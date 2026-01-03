import requests
import json

url = "http://127.0.0.1:8000/api/v1/prompt/generate"

payload = {
    "platform": "chatgpt",
    "goal": "Write a python script to reverse a string",
    "tone": "humorous",
    "complexity": "beginner",
    "prompt_type": "creative",
    "constraints": ["no external libraries"]
}

headers = {
    "Content-Type": "application/json"
}

try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    print("Status Code:", response.status_code)
    print("Response Body:", json.dumps(response.json(), indent=2))
except requests.exceptions.RequestException as e:
    print("Error:", e)
    if hasattr(e, 'response') and e.response is not None:
        print("Error Response:", e.response.text)
