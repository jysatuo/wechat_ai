import os
import requests
import chardet
import json
import io
import re
import time
import gzip

    
def token_size(chat_id, ref_id, token):
   endpoint = f"https://kimi.moonshot.cn/api/chat/{chat_id}/token_size"
   data = {
      "refs": [
        ref_id
      ],
      "content": ""
   }
   res = requests.post(endpoint, data=data, headers={"Authorization": f"Bearer {token}",})
  
   if res.status_code == 200:
      over_size = json.loads(res.text)["over_size"]
      return over_size
   return 0

   
def refresh_kimi_token(key):
    # 授权刷新token
   endpoint = "https://kimi.moonshot.cn/api/auth/token/refresh"
   refresh_token= key["KIMI_REFRESH_TOKEN"]
   res = requests.get(endpoint, headers={"Authorization": f"Bearer {refresh_token}",})
   response = json.loads(res.text)
   key["KIMI_REFRESH_TOKEN"] = response["refresh_token"]
   key["KIMI_TOKEN"] = response["access_token"]    
   filename = f"../ai/key.json"
   with open(filename, 'w') as file:   
      json.dump( key, file)
   return response["access_token"], key

    
def load_kimi_conf(key: tuple, filepath:str, ai_list:list, token: str, ai_param: tuple, kimi_playground: tuple,  kimi_chat_id_dict: dict, wx: str):    
   # kimi_playground是字典，保存各个ai对象的参数
   if wx != "playground":  # 当用户不是在playground进行对话时
      msgid = ai_param['msgid']        
      if not kimi_chat_id_dict.get(msgid):
         endpoint = "https://kimi.moonshot.cn/api/chat"
         res = requests.post(endpoint, json={"name":ai_param.get("name", "未命名会话"), "is_example":False}, headers={"Authorization": f"Bearer {token}",})
         if res.status_code != 200:
            token, key = refresh_kimi_token(key)    
            res = requests.post(endpoint, json={"name":ai_param.get("name", "未命名会话"),"is_example":False}, headers={"Authorization": f"Bearer {token}",})                
         if res.status_code == 200:
            chat_id = json.loads(res.text)["id"]
            kimi_chat_id_dict[msgid] = {'chat_id': chat_id} 
            endpoint = f'https://kimi.moonshot.cn/api/chat/{chat_id}/completion/stream' #导入角色prompt
            if ai_param.get("prompt"):
               res = requests.post(endpoint, json={"messages":[{"role": "user", "content": ai_param["prompt"]}],"refs":[],"use_search":True}, headers={"Authorization": f"Bearer {token}",})
            return token, key, {'chat_id': chat_id}, ai_list, kimi_playground, kimi_chat_id_dict
      else:
         return token, key,  kimi_chat_id_dict[msgid], ai_list, kimi_playground, kimi_chat_id_dict
   else:
      if kimi_playground:
         msgid = ai_param.get('msgid', "playground")     
         if kimi_playground.get(msgid):
            return token, key, kimi_playground[msgid], ai_list, kimi_playground,  kimi_chat_id_dict
         else:
            endpoint = "https://kimi.moonshot.cn/api/chat"
            res = requests.post(endpoint, json={"name": ai_param.get("name", "未命名会话"), "is_example": False}, headers={"Authorization": f"Bearer {token}",})
            if res.status_code != 200:
               token, key = refresh_kimi_token(key)  
               res = requests.post(endpoint, json={"name": ai_param.get("name", "未命名会话"), "is_example": False}, headers={"Authorization": f"Bearer {token}",})                        
            if res.status_code == 200:
               chat_id = json.loads(res.text)["id"]   
               kimi_playground[msgid] = {'chat_id': chat_id}
               endpoint = f'https://kimi.moonshot.cn/api/chat/{chat_id}/completion/stream' #导入角色prompt
               if ai_param.get("prompt"):
                  res = requests.post(endpoint, json={"messages":[{"role": "user", "content": ai_param["prompt"]}],"refs":[],"use_search":True}, headers={"Authorization": f"Bearer {token}",})                                                
               return token, key, {'chat_id': chat_id}, ai_list, kimi_playground, kimi_chat_id_dict            
      else:
         endpoint = "https://kimi.moonshot.cn/api/chat"
         res = requests.post(endpoint, json={"name": ai_param.get("name", "未命名会话"), "is_example": False}, headers={"Authorization": f"Bearer {token}",})
         if res.status_code != 200:
            token, key = refresh_kimi_token(key)  
            res = requests.post(endpoint, json={"name": ai_param.get("name", "未命名会话"), "is_example": False}, headers={"Authorization": f"Bearer {token}",})                        
         if res.status_code == 200:
            chat_id = json.loads(res.text)["id"]
            msgid = ai_param.get('msgid', "playground")            
            kimi_playground = {msgid: {'chat_id': chat_id}}
            endpoint = f'https://kimi.moonshot.cn/api/chat/{chat_id}/completion/stream' #导入角色prompt
            if ai_param.get("prompt"):
               res = requests.post(endpoint, json={"messages":[{"role": "user", "content": ai_param["prompt"]}],"refs":[],"use_search":True}, headers={"Authorization": f"Bearer {token}",})                                                
            return token, key, {'chat_id': chat_id}, ai_list, kimi_playground, kimi_chat_id_dict

        
def ai_assistant(model, messages, ai_param: tuple={"Output Length": 1024, "Temperature": 0.7, "Top-P": 0.7, "Top-K": 50, "Repetition Penalty": 1.01, 'kimi_conf_playground': True}, **kwargs):        
   key = kwargs['key']
   filepath = kwargs['filepath']
   kimi_chat_id_dict = kwargs['kimi_chat_id_dict']
   token = key.get("KIMI_TOKEN")
   token, key, kimi, ai_list, kimi_playground, kimi_chat_id_dict = load_kimi_conf(key, filepath, kwargs['ai_list'], token, ai_param, kwargs['kimi_playground'], kimi_chat_id_dict, kwargs["wx"])
   chat_id = kimi['chat_id']
   if len(kwargs['refs_id'])>=1:
      refs_id = [kwargs['refs_id'][-1]] # 取最后一个
      if refs_id == ["no_content"]:
         content = "文件无法解析文字。"
         messages.append({"content": content, "role": "assistant"})         
         return content, messages, {'key': key, 'ai_list': ai_list, 'kimi_playground': kimi_playground, 'kimi_chat_id_dict': kimi_chat_id_dict}            
      over_size = token_size(chat_id, refs_id, token)
      if over_size > 0: 
         content = "文件过大无法解析，请分割大小后继续上传。"
         messages.append({"content": content, "role": "assistant"})         
         return content, messages, {'key': key, 'ai_list': ai_list, 'kimi_playground': kimi_playground, 'kimi_chat_id_dict': kimi_chat_id_dict}         
   else:
      refs_id = []
   text = messages[-1]
   text['content'] = add_url_tags_to_links(text['content'])
   endpoint = f'https://kimi.moonshot.cn/api/chat/{chat_id}/completion/stream'
   res = requests.post(endpoint, json={"messages":[text],"refs":refs_id,"use_search":True}, headers={"Authorization": f"Bearer {token}",})
   if res.status_code != 200:
      token, key = refresh_kimi_token(key)
      res = requests.post(endpoint, json={"messages":[text],"refs":refs_id,"use_search":True}, headers={"Authorization": f"Bearer {token}",})        
   #print(res.text)
   
   #ret = gzip.decompress(res).decode("utf-8")
   if res.status_code == 200:
      try:
         res.encoding = chardet.detect(res.text)['encoding']
      except:
         res.encoding = 'utf-8'  # 指定编码格式为UTF-8    
      event_stream_data = res.text
      data_stream = io.StringIO(event_stream_data)
      parsed_data = []
      # 逐行读取数据
      for line in data_stream:
         # 移除行尾的换行符
         line = line.rstrip('\n')
         # 如果是数据行（以 "data:" 开头）
         if line.startswith('data:'):
            # 解析数据行，获取 JSON 字符串
            json_str = line.split('data:', 1)[1]
            # 将 JSON 字符串添加到数组中
            parsed_data.append(json_str)        
      # 将 JSON 字符串数组转换为实际的数据对象数组
      data_objects = [json.loads(item) for n, item in enumerate(parsed_data) if n<len(parsed_data)-1]
      content = ""        
      for dict_ in data_objects:
         if dict_["event"] == 'cmpl':
            content_tail = dict_["text"] 
            content = content + content_tail  
      messages.append({"content": content, "role": "assistant"})
      if len(messages) > 15:
         del messages[1]
      if content == "" and kwargs["wx"] == "playground":
         msgid = ai_param.get("msgid", "playground")
         del kimi_playground[msgid]
         messages[-1]["content"] = "本轮会话超出字数限制，即将开启新会话！"
          #content, messages, dict_ = ai_assistant(model, messages[:-1], ai_param, kwargs)     
          #key = dict_['key']
          #ai_list = dict_['ai_list']
          #kimi_playground = dict_['kimi_playground']
          #kimi_chat_id_dict = dict_['kimi_chat_id_dict']
      elif content == "":
         kimi_chat_id_dict[ai_param['msgid']] = {} 
         messages[-1]["content"] = "本轮会话超出字数限制，即将开启新会话！"            
          #content, messages, dict_ = ai_assistant(model, messages[:-1], ai_param, kwargs)     
          #key = dict_['key']
          #ai_list = dict_['ai_list']
          #kimi_playground = dict_['kimi_playground']
          #kimi_chat_id_dict = dict_['kimi_chat_id_dict']            
      return content, messages, {'key': key, 'ai_list': ai_list, 'kimi_playground': kimi_playground, 'kimi_chat_id_dict': kimi_chat_id_dict}
   content = "网络繁忙，稍后再试"
   return content, messages, {'key': key, 'ai_list': ai_list, 'kimi_playground': kimi_playground, 'kimi_chat_id_dict': kimi_chat_id_dict}


def ai_assistant_upload_file(filepath, key):
   time.sleep(5)
   token = key["KIMI_TOKEN"]
   endpoint = "https://kimi.moonshot.cn//api//pre-sign-url"    
   file = open(filepath, 'rb')
   file_name = re.search(r'[^\\//]+$', file.name).group()
   # 创建一个带有文件的请求数据
   res = requests.post(endpoint, data={"action":"file","name":file_name}, headers={"Authorization": f"Bearer {token}" })
   if res.status_code != 200:
      token, key = refresh_kimi_token(key)
      res = requests.post(endpoint, data={"action":"file","name":file_name}, headers={"Authorization": f"Bearer {token}" }) 
   if res.status_code == 200:
      data = json.loads(res.text)
      object_name = data["object_name"]
      url = json.loads(res.text)["url"]
      res = requests.put(url, data=file, headers={"Authorization": f"Bearer {token}",})
      file.close()
      endpoint = "https://kimi.moonshot.cn/api/file"
      data = {"type":"file","name":file_name,"object_name":object_name}            
      res = requests.post(endpoint, json=data ,headers={"Authorization": f"Bearer {token}",})
      if res.status_code != 200:
         token, key = refresh_kimi_token(key) 
         res = requests.post(endpoint, json=data ,headers={"Authorization": f"Bearer {token}",})
      if res.status_code == 200:
         data = json.loads(res.text)
         ref_id = data['id']
         endpoint = "https://kimi.moonshot.cn/api/file/parse_process"  
         res = requests.post(endpoint, json={"ids":[ref_id]} ,headers={"Authorization": f"Bearer {token}",})
         if res.status_code == 200:
            line = res.text
            json_str = line.split('data:', 1)[1]
            res_parse = json.loads(json_str)     
            if res_parse["status"] == "failed":
               return "no_content", key
         return ref_id, key
      return None, key


def add_url_tags_to_links(text):
   pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+/?[^\s]*'
   def replace_link_with_tags(match):
       #return f'<url>{match.group(0)}</url>'
      return f'<url id=\"\" type=\"url\" status=\"\" title=\"\" wc=\"\">{match.group(0)}</url>'
   result = re.sub(pattern, replace_link_with_tags, text)
   return result


# 把微信图片转化出来（dat->jpg）
def Format(f):
   dat_r = open(f, "rb")
   try:
      a = [(0x89, 0x50, 0x4e), (0x47, 0x49, 0x46), (0xff, 0xd8, 0xff)]
      for now in dat_r:
         for xor in a:
            i = 0
            res = []
            nowg = now[:3]
            for nowByte in nowg:
               res.append(nowByte ^ xor[i])
               i += 1
            if res[0] == res[1] == res[2]:
               return res[0]
   except Exception as e:
      print(e)
   finally:
      dat_r.close()

def convertDatToImage(dat_file_path, save_path):
   xo = Format(dat_file_path)
   out_file = os.path.join(save_path, os.path.basename(dat_file_path)[:-4] + ".jpg")
   dat_read = open(dat_file_path, "rb")
   png_write = open(out_file, "wb")

   for now in dat_read:
      for nowByte in now:
         newByte = nowByte ^ xo
         png_write.write(bytes([newByte]))

   dat_read.close()
   png_write.close()
   
   
   
def ai_assistant_upload_image(filepath, key):
   file_extension = os.path.splitext(filepath)[1][1:]
   if file_extension == "dat":
      time.sleep(3)
      folder_location = os.path.dirname(filepath)   
      convertDatToImage(filepath, folder_location)
      file_name = os.path.splitext(os.path.basename(filepath))[0]+ ".jpg"
      file_path = f"{folder_location}\\{file_name}"
      file = open(file_path, 'rb')
   else:
      file_name = re.search(r'[^\\//]+$', filepath).group()      
      #file_name = os.path.splitext(os.path.basename(filepath))[0]      
      file = open(filepath, 'rb')
   token = key["KIMI_TOKEN"]
   endpoint = "https://kimi.moonshot.cn//api//pre-sign-url"    
   # 创建一个带有文件的请求数据
   res = requests.post(endpoint, data={"action":"file","name":file_name}, headers={"Authorization": f"Bearer {token}" })
   if res.status_code != 200:
      token, key = refresh_kimi_token(key)
      res = requests.post(endpoint, data={"action":"file","name":file_name}, headers={"Authorization": f"Bearer {token}" }) 
   if res.status_code == 200:
      data = json.loads(res.text)
      object_name = data["object_name"]
      url = json.loads(res.text)["url"]
      res = requests.put(url, data=file, headers={"Authorization": f"Bearer {token}",})
      file.close()
      endpoint = "https://kimi.moonshot.cn/api/file"
      data = {"type":"file","name":file_name,"object_name":object_name}            
      res = requests.post(endpoint, json=data ,headers={"Authorization": f"Bearer {token}",})
      if res.status_code != 200:
         token, key = refresh_kimi_token(key) 
         res = requests.post(endpoint, json=data ,headers={"Authorization": f"Bearer {token}",})
      if res.status_code == 200:
         data = json.loads(res.text)
         ref_id = data['id']
         endpoint = "https://kimi.moonshot.cn/api/file/parse_process"  
         res = requests.post(endpoint, json={"ids":[ref_id]} ,headers={"Authorization": f"Bearer {token}",})
         if res.status_code == 200:
            line = res.text
            json_str = line.split('data:', 1)[1]
            res_parse = json.loads(json_str)     
            if res_parse["status"] == "failed":
               return "no_content", key
         return ref_id, key
      return None, key