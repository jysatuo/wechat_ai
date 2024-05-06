# -*- coding:utf-8 -*-
import requests
import json
import random
import os
import io
import chardet


token_url = "https://web.stytch.com/sdk/v1/sessions/authenticate"
def getAnontoken(authorization :str="eyJldmVudF9pZCI6ImV2ZW50LWlkLWNlZTQyOWY4LTc3YzMtNGE5Ny1hZGMyLTI5NDZjMzJlMjdiOSIsImFwcF9zZXNzaW9uX2lkIjoiYXBwLXNlc3Npb24taWQtNzAyYmQ5MzMtMDk1OS00ZTBkLWJmYjQtMzM1NTYxMDAzZGE3IiwicGVyc2lzdGVudF9pZCI6InBlcnNpc3RlbnQtaWQtZThkMzJmYzEtNWU3Zi00YWIwLTk1N2ItODBlMzA2NjI1Mzg2IiwiY2xpZW50X3NlbnRfYXQiOiIyMDI0LTA0LTI5VDAyOjMzOjE5LjY0M1oiLCJ0aW1lem9uZSI6IkFzaWEvU2hhbmdoYWkiLCJzdHl0Y2hfdXNlcl9pZCI6InVzZXItbGl2ZS0xNmI1ODQ3Mi04MDU0LTQxYTItODlkYi1iMDQ1MTVmNTdkZDkiLCJzdHl0Y2hfc2Vzc2lvbl9pZCI6InNlc3Npb24tbGl2ZS1hNDFkOWZhZi1hODg3LTQ3M2UtOGIzNy1lYjJjMWY2NzRmYTAiLCJhcHAiOnsiaWRlbnRpZmllciI6Imdyb3EuY29tIn0sInNkayI6eyJpZGVudGlmaWVyIjoiU3R5dGNoLmpzIEphdmFzY3JpcHQgU0RLIiwidmVyc2lvbiI6IjQuNi4wIn19"):
    res = requests.post(token_url, data='{}',headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36","authorization": "Basic cHVibGljLXRva2VuLWxpdmUtMjZhODlmNTktMDlmOC00OGJlLTkxZmYtY2U3MGU2MDAwY2I1OmNweE90RDdLaXZzTlpmNzFwVWJ2RFIyTHJzMjluWEFGZDl3WGZyTGNTZnYx","origin": "https://groq.com","referer": "https://groq.com/","accept": "*/*", "content-length": "2", "content-type": "application/json", "x-sdk-client":authorization, "x-sdk-parent-host": "https://groq.com", "sec-ch-ua-platform": 'Windows', "sec-fetch-site": "cross-site", "Host":"web.stytch.com"})    
    dict_ = json.loads(res.text)
    return dict_["data"]["session_jwt"]


#endpoint = 'https://api.groq.com/v1/request_manager/text_completion'
#endpoint = 'https://groq.jysatuo.workers.dev/openai/v1/chat/completions'
endpoint = 'https://api.groq.com/openai/v1/chat/completions'
#endpoint = "https://groq.xunai.xyz/openai/v1/chat/completions"


def ai_base(model, token, messages, ai_param):
    res = requests.post(endpoint, json={
        "model": model,
        "messages": messages,
        "temperature": ai_param["Temperature"],
        "max_tokens": ai_param["Output Length"],
        "top_p": ai_param["Top-P"],
        "stream": True
        }, headers={
        "content-type":"application/json;charset=UTF-8",
        "groq-organization": "org_01hs8zn0fzegjs37wqqa17hz4g",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        "authorization": f"Bearer {token}",
    })
    if res.status_code == 200:
        res.encoding = chardet.detect(res.content)['encoding']  
    return res

def ai_assistant(model, messages, ai_param, key):    
    token = key['GROQ_TOKEN']
    res = ai_base(model, token, messages, ai_param)
    content = ""    
    if res.status_code == 200:
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
        for dict_ in data_objects:
            content_tail = dict_["choices"][0]["delta"].get("content")
            if content_tail and content_tail is not None:
                content = content + content_tail            
    elif res.status_code == 401:
        token = getAnontoken()
        save_token(token)
        key["GROQ_TOKEN"] = token        
        res = ai_base(model, token, messages, ai_param)        
        if res.status_code == 200:
            event_stream_data = res.text
            data_stream = io.StringIO(event_stream_data)
            parsed_data = []
            for line in data_stream:
                line = line.rstrip('\n')
                if line.startswith('data:'):
                    json_str = line.split('data:', 1)[1]
                    parsed_data.append(json_str)            
            data_objects = [json.loads(item) for n, item in enumerate(parsed_data) if n<len(parsed_data)-1]            
            for dict_ in data_objects:
                content_tail = dict_["choices"][0]["delta"].get("content")
                if content_tail and content_tail is not None:
                    content = content + content_tail
    messages.append({"content": content, "role": "assistant"})
    if len(messages) > 10:
        del messages[1]
    return content, messages, {'key': key}

def load_token():
    with open("../ai/key.json", "r") as f:
        file = f.read()
        key = json.loads(file)
        return key["GROQ_TOKEN"]
    return ""
    
    
def save_token(token):
    with open("../ai/key.json", "r") as f:
        file = f.read()    
        key = json.loads(file)
        key["GROQ_TOKEN"] = token
    with open("../ai/key.json", "w") as f:
        json.dump(key, f)     
                
    
if __name__ == "__main__":
    token = "eyJldmVudF9pZCI6ImV2ZW50LWlkLWQzNzkyY2E4LTM5YWYtNGE3NS1hMmZlLWMwZWYzODE3MjFkOCIsImFwcF9zZXNzaW9uX2lkIjoiYXBwLXNlc3Npb24taWQtYjA1NjdkOGUtNWY3MS00N2UxLWFmOTctZTFlZDdhODVmNGRmIiwicGVyc2lzdGVudF9pZCI6InBlcnNpc3RlbnQtaWQtNTRkZTViOTAtMzFmZS00Y2ExLThhNDAtODMxZWExMTg2Y2NjIiwiY2xpZW50X3NlbnRfYXQiOiIyMDI0LTAzLTE5VDE4OjIyOjE4LjY5NloiLCJ0aW1lem9uZSI6IkFzaWEvU2hhbmdoYWkiLCJzdHl0Y2hfdXNlcl9pZCI6InVzZXItbGl2ZS0xNmI1ODQ3Mi04MDU0LTQxYTItODlkYi1iMDQ1MTVmNTdkZDkiLCJzdHl0Y2hfc2Vzc2lvbl9pZCI6InNlc3Npb24tbGl2ZS1iYTNhNmQ3Zi1jY2QxLTRjMzItYmY2Ny1hNzQ0Yjk3MmY3MmQiLCJhcHAiOnsiaWRlbnRpZmllciI6Imdyb3EuY29tIn0sInNkayI6eyJpZGVudGlmaWVyIjoiU3R5dGNoLmpzIEphdmFzY3JpcHQgU0RLIiwidmVyc2lvbiI6IjQuNS4zIn19"
    messages = [
    {
      "content": "脑筋急转弯大师.",
      "role": "system"
    },
    {
      "content": "用中文介绍下自己",
      "role": "user"
    }]
    output = ai_assistant(model,token, messages)    
    print(output)
