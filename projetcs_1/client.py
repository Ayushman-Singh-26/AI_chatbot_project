import requests
import json

API_KEY = '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'
MODEL_ID = 'gpt2'

url = f"https://api-inference.huggingface.co/models/{MODEL_ID}"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

data = {
    "inputs": "Write a haiku about recursion in programming."
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    print(f"Generated text: {result[0]['generated_text']}")
else:
    print(f"Error: {response.status_code}")
    print(f"Details: {response.text}")
