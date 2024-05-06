import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import os
import requests
import json

with open("../ai/key.json","rb") as f:                                
    file = f.read()
    key = json.loads(file)    
    genai.configure(api_key=key["GEMINI_API_KEY"])
#genai.configure(api_key="AIzaSyB7k6UZoCVy9pNMjCiim4VqSJduPSRdpog")


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


def ai_assistant(model, messages, ai_param:tuple={"Output Length": 1024, "Temperature": 0.7, "Top-P": 0.7, "Top-K": 50, "Repetition Penalty": 1.01}):
    model = genai.GenerativeModel('gemini-pro')
    start_role = 'user'
    gemini_messages = []
    for message in messages:
        if message['role'] == start_role:
            if start_role == "assistant":
                gemini_messages.append({'role':"model", 'parts': [message['content']]})
            else:
                gemini_messages.append({'role':start_role, 'parts': [message['content']]})
            start_role = 'user' if start_role=="assistant" else 'assistant'  
        elif message['role'] == "system":
            gemini_messages.append({'role': "user", 'parts': [message['content']]})
            gemini_messages.append({'role': "model", 'parts': ["好的，严格按照以上的角色要求进行对话。"]})
            
    response = model.generate_content(gemini_messages)
    content = response.text
    messages.append({"content": content, "role": "assistant"})
    if len(messages) > 15:
        del messages[1]
    return content, messages 
