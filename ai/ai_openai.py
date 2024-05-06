# -*- coding:utf-8 -*-
 

import requests
import json
import random
import io
import os

os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"

#url = "https://chat.freegpts.org/backend-api/conversation"


url = "https://chat.openai.com/backend-api/conversation"

headers={
    #eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJqeXNhdHVvQG91dGxvb2suY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsicG9pZCI6Im9yZy1rck5jWGJVdkJ4NHNoYkVBQk1CMmQ0bE8iLCJ1c2VyX2lkIjoidXNlci1QS0VsMFVhcU96YUVjR0JnTEFqMWY2VUEifSwiaXNzIjoiaHR0cHM6Ly9hdXRoMC5vcGVuYWkuY29tLyIsInN1YiI6ImF1dGgwfDY1Zjg2ZDU1ZDgxMGU4MGE3M2EzZjI3YSIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkub3BlbmFpLmF1dGgwYXBwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3MTA3Nzk4NTcsImV4cCI6MTcxMTY0Mzg1NywiYXpwIjoiVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEciLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG1vZGVsLnJlYWQgbW9kZWwucmVxdWVzdCBvcmdhbml6YXRpb24ucmVhZCBvcmdhbml6YXRpb24ud3JpdGUgb2ZmbGluZV9hY2Nlc3MifQ.xXCMMzQhj3vCujibdUz6eR6xuIlcKrMrwaCvmvGIp6b6VNTCQLvPCaNz8dQyC5BYT2j9OLGcdCBEuN-iMjZLdvJgO2Lz-HgtaTt1MO-0Yish6oQ52ObMqiVLmF7n_2hNYh-alLoYzYAQFVnQk42u5Kz-j3lpHmAipOtCZ98mX9weVs7XvLSqmypWB2zQo8v0dIwVwjdrqGn7LKheRdGYVMFmsd2F5YHYVzxL7-GVsA-urtI-b7ExMeHW8Llf_V0pbpnCBJVTH500ef59S01kzuvM3pliZRg9HRaArXrKJqWQNENC2-HF-XYQM7BL-t42l1Q6DoEMIah-5kY6M51AvQ
    
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJqeXNhdHVvQG91dGxvb2suY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsicG9pZCI6Im9yZy1rck5jWGJVdkJ4NHNoYkVBQk1CMmQ0bE8iLCJ1c2VyX2lkIjoidXNlci1QS0VsMFVhcU96YUVjR0JnTEFqMWY2VUEifSwiaXNzIjoiaHR0cHM6Ly9hdXRoMC5vcGVuYWkuY29tLyIsInN1YiI6ImF1dGgwfDY1Zjg2ZDU1ZDgxMGU4MGE3M2EzZjI3YSIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkub3BlbmFpLmF1dGgwYXBwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3MTA3Nzk4NTcsImV4cCI6MTcxMTY0Mzg1NywiYXpwIjoiVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEciLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG1vZGVsLnJlYWQgbW9kZWwucmVxdWVzdCBvcmdhbml6YXRpb24ucmVhZCBvcmdhbml6YXRpb24ud3JpdGUgb2ZmbGluZV9hY2Nlc3MifQ.xXCMMzQhj3vCujibdUz6eR6xuIlcKrMrwaCvmvGIp6b6VNTCQLvPCaNz8dQyC5BYT2j9OLGcdCBEuN-iMjZLdvJgO2Lz-HgtaTt1MO-0Yish6oQ52ObMqiVLmF7n_2hNYh-alLoYzYAQFVnQk42u5Kz-j3lpHmAipOtCZ98mX9weVs7XvLSqmypWB2zQo8v0dIwVwjdrqGn7LKheRdGYVMFmsd2F5YHYVzxL7-GVsA-urtI-b7ExMeHW8Llf_V0pbpnCBJVTH500ef59S01kzuvM3pliZRg9HRaArXrKJqWQNENC2-HF-XYQM7BL-t42l1Q6DoEMIah-5kY6M51AvQ", #"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJzc2FhYTAxMjNAcHJvdG9uLm1lIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsicG9pZCI6Im9yZy0zUVlhVDNGajczaW5UU3ZGdE96cTNKdWoiLCJ1c2VyX2lkIjoidXNlci1DUnVVZ1hSS0NDVXA0a0ZqTG5nRVlZNXkifSwiaXNzIjoiaHR0cHM6Ly9hdXRoMC5vcGVuYWkuY29tLyIsInN1YiI6ImF1dGgwfDY1N2MyYTQzYTVlY2Q4NTM5MWI2MTFhMyIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkub3BlbmFpLmF1dGgwYXBwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3MTA2MDg1MjgsImV4cCI6MTcxMTQ3MjUyOCwiYXpwIjoiVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEciLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIG1vZGVsLnJlYWQgbW9kZWwucmVxdWVzdCBvcmdhbml6YXRpb24ucmVhZCBvcmdhbml6YXRpb24ud3JpdGUgb2ZmbGluZV9hY2Nlc3MifQ.ts21jxrY6VjoNl5oItx5ZwLaWLF4lGjOmNxcJEvaqdLabXC2C78lQq3qzFF_mFDZn3KMVQmxWBsyVm8wOW4PUL4XaS4xH0kBoo5Dz-h2tFNrubkE_OLI1-tf7QOfKWgL3Gi__kW-WdjOH71Zf5rGhumiqDfBAD0PeCSmkSAKTQDTrO5IW6TepgkBoUf2fFY7lNRNVwoKJrLD-QZU-roY1hhgE5K0ouwEsqaNVs5_6qFUxk92EFar7S6RjWmo-CikzVB2-_wEnDzcZy8zhue2Eb2mN5tG_6N-Z7FJxb0vy3w7R5XsDagphWqhhQfdLJLjj-wkCvdm_Bio7zGfJWoCfA",        "Accept": "text/event-stream",
       
        #"OpenAI-Sentinel-Chat-Requirements-Token": "gAAAAABl9dC2LaOGVgEIKSx7m-wyc1BuWRpTY1HjFB9bDWDCVp35j08CH2wtqivFBVtg_569TO0gt2bysll5XxS78_ntEy83SK_4eiVuTNiRYcow6IvY7MUW_hYvZ7RCGgMMmDFvK1E_aErou5RQE0SS7xulM-ZzX14TNkq3-HHEzXaeTUO4FB12Xzg25JqSXliqE1c08SUr2o0f_ZLMQ7O88GGs4nZvVHxvpxW1teEW9Jww_GqxsBiutoBPMQo99HQmddJvHztFLSVOgMfyDJnD_BbJmgMlbQ==",
        #"Sec-Fetch-Site": "same-origin",       
        #"OAI-Language": "en-US",
        #"OAI-Device-Id": "816fc02c-c278-46f7-993d-0388773112d0",
        #"Accept-Language": "zh-CN,zh-Hans;q=0.9",
        #"Sec-Fetch-Mode": "cors",
        #"Accept-Encoding": "gzip, deflate, br",
        #"Origin": "https://chat.freegpts.org",
        ##"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Mobile/15E148 Safari/604.1",
        #"Referer": "https://chat.freegpts.org/c/f2cc74f9-745c-4241-8a8a-f1c3d8060ee1",
        #"Content-Length": "588",
        #"Connection": "keep-alive",
        "Content-Type": "application/json",
        #"Sec-Fetch-Dest": "empty",
        #"Cookie": "_dd_s=rum=0&expire=1710932287000; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..t9A00DMf6GpgTqkO.dH7csvvdSsNr1n1ueaRa8ulvyzbrZL9gYZLiLZZzSh6jm_hyy2cZ5uRv0Z6XLwqUjJwrXINGCzrNSDmylgYBEJZ9r7761ZMC-5k2lJKGo8VNPpsLq1w9P2NyjI33CRDS6h0QVASnNiNdgNVZByw3yhmO0b8hxC0wamrXSjkoCbsYbln2oMRluZ6ren4-6NXEkhbge_agdqvSc_fxYnqnEqjYcryDcbhPB42oaYin5nHjCiBnJzF5QW2jSTI7gDy2SqONqTd8wQMANak6rUv2KvOvXygGlPVuyYRvVGdydW8nkAtsn-u7frcaDx24ZWcIHxI9eJ6ZF9hTGnwUVWTOc_ar_hKS18IuBnyna3FX-HAk9fAjNnYsql95jeWq1VuLQEo_dCbzgFd0XK95v6t8j55etGvN0sQJT6UJZ5-odzdqiGyKh4OqUClzazf3Qg-fF1V-FQs9vVKKPPgbNOUW8f1Y7UFXyv9gi6Lm-IbFN9CSnsfyrNtjryaxSpe_qmXSVq5iFjMjF2Q6PxtWn0uB2EirYwJjGd0rFE2EKEgOrB1QvZzPTf5OB36WSHAc-dProNxHzLbbKr0ThxpTaIdm2r2otsIclVfUiMVvsvYMMOsd2Z621iR6Pzp9jv2n-YvaY6lL8KwslF_PSQ5WtFH_6n7cxMVYD4PEHr2fFKQyfGhG53F7QV6voUHOF7l0j3arJfZdzv6fHIJKmVGbFP7I4YmMivDIzA2eYHUEhwOVrPG37dSIrR1BSrCNkX3hBzJlrxXuvnqmTyUyuPBaMaCRb8pVDV_5-KwlabNMHmeiUPWMN9z-WIcWQV5hQN8VrCKu0BKGMxSwG66ttmOd1r4v2NAujthhF1VIXohWDfpJaYAtLhgaTcJjV9nwvfoUd1xS_Px2AIr1gi3YAUq4t7PbxmtH-aaYAX7o6SY4Bhp4vESku6XmDzesFJLYE9Wz8wk12ycSqQ71OQntQl2R3L3DEHJQJVovlCWRMImunYzi1uOMLx-rzRpqjDJ1ukEVtVfbzfHOloGgNM6fdEgYOA_Ltn9tWKv0bPMu0EVrntyUHVAyJDdsh51oQedXBduOm_advUiJ8zpib73EZPnbsH6SPDLyNkI_8uxMH8_goAkDDEjHA0021OjTVE2Gq2xTewwvpJtRLlxU9ZOkXzqncGGsy2zRJUvaoZ1vSdAs3_Rn6O4wXpPTQzo8EkASL602vVBKCJzioBMY_Gp4v74HQuxnvgE-KJ-SL1kQ32e7y-Xg9wC3aY1ExI3lJe0KLg3BA1z8L2HHKH1mYf9ebqJPSr_gIFSlPr7wzQsjj3gYg90zKunWdiv0PYoD89ThZr1wBLumjBQo62n1HGhrK5zH9pbqFoDViJPQf9Kd2D8SVn5kaVhYVsIHnlZPG_iLNdkLzVxuGWllzVRd__ctqJj4SCbz2V82TMc3TJZ2DCyRqRsh8kw-iOYMg41jzxuAIZLBIosRt_GLegGfXIpU_1xb4Z3cDCmXvly9_h1pr05wwoLJ_bc8wkED4whBAugrZmBl9UXERJEmbpsoOMReMUMnlG7hhbGqzDdvhcgY8oMdY5OAxV86xWAqPtkrPanDf7PB8uTqIIATfOBUxF4CO6WTJ-q3PSJM9YcA5fGM47saRBP_GHhrCfLgs73zhkFf0mwVXTw3fnxWLns7hrz5kxPaMxA35nyz3R0HPr5Io-KmtJkI_aRCdKojfht8jx1IA5arlyPXT-1qkgerTrHuRqdGMK57ligbcNTxdGy5v95J19fNTQho6Llj60H9EE1TcEkPsR3qzwDPE5nBl7vbQPta8JNl4wSQpsIk-Scraivb0x8sbwIXSieyq1Lq7K4hzikIWgk7N1Q-4j0mR_yujpr7HxzyYmAE7Q0erv0f78OeWRmQIg6b9VT8viWDG9jQRPZkN0c-Z_wmF5oPleoxhU_3-0foTxQ3Bt2bGzJhFloXvbejCnq2EvcXI5lnm3J1FV5Sn-y_ehuJ9B_S3pM2TxbnkpUc-VCrn025fsps2S47w3w2tYzXwt0PctUF9P2DT6yOa686bZjlSmtJldHGkXEQbGPfBcoCvgLDle_O8xQR3QGOuTDbjoFRP0GK4wRjgnrzCqqxkp0OL90Jb5DYJFd95ecuU9ktrwUZKCQ6ByEWOMhrBdZiXgSXHumcF27Q638u6P-r4Y84SuR4fLEcYQIXK97kTrcBBdEHsuDIJBv-2NhF7mWciNb-d4hNg3o8erf4S_cW6XHf5V-doQglue7otOpNToo45qugU-RFLNF5BDlE_p7E-ytN4JAwwsT-sUNiBDBM50Uubcw8OPlkUTf54BGSA-m4EQfrgLbPpBmPu1cH35dxF1aeG2N3MwGmDixZhuOxyWbQRhz9BY53ANkLRPSkbMH_j4BzS-zQJtFgOjsoFS83PPM86j5HM1KV-IK810cvV0tG9-p-wtJkBEDh35LM7yss-RcLJiXMwJ3ewh9iX5tPgDi8Vk0nNsABP00IaHB5OW_-akW81PBk3ET11El6p1yY8Hl5ys7VvBncsKvGX9yXCIMVpIhOr3-Jqinwc5I52WpuS2FHjjfsgHIwOTPs9u-MA6P8YGAlBfpbK-GEkYf5BYWFmMF9CfL7wzaXbMnCtbMJZw9XCioul0Kl4SWW2roJrGCNboA_i6auoKB6Z7An-7w23bABzuxxdlwg51JnoHaKExpBV7Jpaew683lYXhFdJg-3C0Cy_ha_AOyb-30Wqxjwg6r6BmBf2TtkjO_u-9BrHcz5-QkyUJg9296LZDGA2E6RndNwLRbunloI_LB3z58RHij6Ea_X7BRV_Upa0hhVuBzChON7CYLP1Ulqr0PCBO8TVk6eQnsmo_lb4qCZTyjrl2AC-Wl5WTvyODc2yHFEXhaYQKvbGFK4x5e2u0b-npOPW1JBlFdI0g.ITwLRr50EpZFf9eUnz5SRg;timestamp=1710608515177;xy-arkose-session=2imt1205av6x80czvc1j34yf41ctys0m;lb-session=r54iew01ssv5qsczvc1hv159ri2e22kf"
    }

def getAnontoken():
    data = {"action":"next","messages":[{"id":"aaa2cd73-2f11-40ce-a06a-c514684cb791","author":{"role":"user"},"content":{"content_type":"text","parts":["如何让ai和社交结合起来"]},"metadata":{}}],"conversation_id":"f2cc74f9-745c-4241-8a8a-f1c3d8060ee1","parent_message_id":"91bdb264-0cf5-453a-94b0-32007f51df0a","model":"text-davinci-002-render-sha","timezone_offset_min":-480,"suggestions":[],"history_and_training_disabled":"false","conversation_mode":{"kind":"primary_assistant"},"force_paragen":"false","force_rate_limit":"false","websocket_request_id":"5a77fa3f-e20f-479d-8acd-1508764e0dc3"}
    print('ssds')
    #res = requests.get(url)
    res = requests.post(url, json=data, headers=headers)
    print(res)
    print('2323')
    dict_ = json.loads(res.text)
    print(dict_)
    return dict_

 

#MODEL = "mixtral-8x7b-32768"
#endpoint = 'https://api.groq.com/v1/request_manager/text_completion'

#def gpt(token, prompt):    
    #res = requests.post(endpoint, json={
        #"model_id": MODEL,
        #"history": [],  # [{"assistant_response":"XXX","user_prompt":"xxx"}]
        #"max_input_tokens": 21845,
        #"max_tokens": 1024,
        #"temperature": 0.2,
        #"top_p": 0.8,
        #"top_k": 40,
        #"seed": 10,
        #"system_prompt": "Please try to provide useful, helpful and actionable answers.",
        #"user_prompt": prompt,
    #}, headers={
        #"Host": "api.groq.com",
        #"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        #"authorization": f"Bearer {token}",
    #})
    
    #if res.status_code == 200:
        #content = ""
        #data = res.text.split("\n")
        #for str_ in data[2:-2]:
            #print(str_)
            #dict_ = json.loads(str_)
            #content = content + dict_["result"]["content"]
        
        #return content
    #else:
        #return ""
    
    
if __name__ == "__main__":
    #output = getAnontoken()
    print(url)
    payload = {"action":"next","messages":[{"id":"aaa2ba0e-afa3-41b3-af4f-011ceeefbfbe","author":{"role":"user"},"content":{"content_type":"text","parts":["如何腌制牛肉干"]},"metadata":{}}],"parent_message_id":"aaa1a3d2-ea51-4191-933e-f2db9d0711dd","model":"text-davinci-002-render-sha","timezone_offset_min":-480,"suggestions":["Brainstorm 5 episode ideas for my new podcast on urban design.","Write a text asking a friend to be my plus-one at a wedding next month. I want to keep it super short and casual, and offer an out.","Compare shifting business strategies from budget to luxury and luxury to budget, using a brief table to outline different aspects","Create a charter to start a film club that hosts weekly screenings and discussions"],"history_and_training_disabled":False,"conversation_mode":{"kind":"primary_assistant"},"force_paragen":False,"force_rate_limit":False,"websocket_request_id":"cee9bedf-0fc6-43a7-9800-f3463f2d5e7d"}
    #payload = {"action":"next","messages":[{"id":"aaa2cd73-2f11-40ce-a06a-c514684cb791","author":{"role":"user"},"content":{"content_type":"text","parts":["如何让ai和社交结合起来"]},"metadata":{}}],"conversation_id":"","parent_message_id":"a1a2ba0e-afa3-41b3-af4f-011ceeefbfbe","model":"text-davinci-002-render-sha","timezone_offset_min":-480,"suggestions":[],"history_and_training_disabled":"false","conversation_mode":{"kind":"primary_assistant"},"force_paragen":"false","force_rate_limit":"false","websocket_request_id":"5a77fa3f-e20f-479d-8acd-1508764e0dc3"}
    
    #payload = {"action":"next","messages":[{"id":"aaa2cd73-2f11-40ce-a06a-c514684cb791","role":"user","content":{"content_type":"text","parts":["如何让ai和社交结合起来"]}}],"conversation_id":"","parent_message_id":"aaa2ba0e-afa3-41b3-af4f-011ceeefbfbe","model":"text-davinci-002-render-sha"}
    #payload = {"metadata":{},"id":"aaa2a1a9-59e3-4ce5-9f4d-6d567ec96c2a","author":{"role":"user"},"content":{"parts":["你上一个问题是什么"],"content_type":"text"}}
    print(payload)
    #print(res)
    #dict_ = json.loads(res.text)
    #print(dict_)
    #output = gpt(getAnontoken(), "我想在中国的一个城市旅游，第一步帮我随机选择一个城市，第二步规划旅游路线方案。用中文进行回答。格式：城市：攻略：")    
    #payload = {"action":"next","messages":[{"id":"aaa2cd73-2f11-40ce-a06a-c514684cb791","author":{"role":"user"},"content":{"content_type":"text","parts":["如何让ai和社交结合起来"]},"metadata":{}}],"conversation_id":"f2cc74f9-745c-4241-8a8a-f1c3d8060ee1","parent_message_id":"91bdb264-0cf5-453a-94b0-32007f51df0a","model":"text-davinci-002-render-sha","timezone_offset_min":-480,"suggestions":[],"history_and_training_disabled":"false","conversation_mode":{"kind":"primary_assistant"},"force_paragen":"false","force_rate_limit":"false","websocket_request_id":"5a77fa3f-e20f-479d-8acd-1508764e0dc3"}
 
    response = requests.post(url, headers=headers, json=payload, allow_redirects=False,verify=False)
    print(response)
    print(response.text)
    print(type(response.text))
    event_stream_data = response.text
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
    
    #print(parsed_data)
    
    # 将 JSON 字符串数组转换为实际的数据对象数组
    data_objects = [json.loads(item) for n, item in enumerate(parsed_data) if n<len(parsed_data)-1]
     
    # 输出转换后的数据
    print(data_objects)