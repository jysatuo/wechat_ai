# -*-coding:utf-8 -*-

import os
import json

def load_history(filepath):
    if os.path.isfile(filepath + "ai_history.json"):
        with open(filepath + "ai_history.json", "r") as f:
            file = f.read()
            if len(file) > 0:
                messages = json.loads(file)
            else:
                messages = []     
    else:
        messages = []   
    return messages

def save_history(filepath, messages):
        with open(filepath + "ai_history.json", "w" ) as f:
            json.dump(messages, f)     

def load_messages_dict(filepath, ai_list):
    filepath = f"{filepath}/messages"
    messages_dict = {}
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    for ai in ai_list:
        filename = ai["msgid"]
        if os.path.isfile(f"{filepath}/{filename}.json"):
            with open(f"{filepath}/{filename}.json", "r") as f:
                file = f.read()
                if len(file) > 0:
                    messages = json.loads(file)
                else:
                    messages = [{"content":ai["prompt"],"role":"system"}]     
        else:
            messages = [{"content":ai["prompt"],"role":"system"}] 
        messages_dict[ai["msgid"]] = messages
    return messages_dict

            
def save_messages_dict(filepath, messages_dict):
    for filename, messages in messages_dict.items():
        with open(f"{filepath}/messages/{filename}.json", "w" ) as f:
            json.dump(messages, f) 
         