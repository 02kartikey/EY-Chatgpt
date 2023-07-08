import requests
import openai
URL = "https://api.openai.com/v1/chat/completions"

payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "What is the first computer in the world?"}],
    "temperature": 1.0,
    "top_p": 1.0,
    "n": 1,
    "stream": False,
    "presence_penalty": 0,
    "frequency_penalty": 0,
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer OPENAPIKEY" #Note key will be with bearer only, format will be ""bearer -key-"" 
}

response = requests.post(URL, headers=headers, json=payload)
print(response.content)