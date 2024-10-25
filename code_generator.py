import base64
import requests
import json
import time
from jarvis_assistant import *
from local_keys import *

def generate_code(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4",
        "messages": [{"role": "user", "content": f"{prompt}\n\nPlease provide only the code without comments or explanations. Never use more than one file, always combine into one file. Never return anything but code. No response other than code. Only the code no explaination or any other text or label. You may use comments if you have to but everything you return will go into github."}],
        "max_tokens": 500,
        "temperature": 0.5,
        "n": 1
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    
    if response.status_code == 200:
        code = response.json()["choices"][0]["message"]["content"].strip()
        return code
    else:
        print("Error generating code:", response.json())
        return None

def save_code_to_github(code):
    """Save generated code to a GitHub repository."""
    timestamp = int(time.time())
    file_name = f"generated_code_{timestamp}.py"
    url = f"{GITHUB_API_URL}/repos/{REPO_NAME}/contents/{file_name}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }
    
    # Base64 encode the code content
    content_base64 = base64.b64encode(code.encode()).decode()

    data = {
        "message": f"Create code file: {file_name}",
        "content": content_base64,
    }
    
    response = requests.put(url, json=data, headers=headers)
    if response.status_code not in (201, 200):  # Check for success
        print("Error creating or updating file:", response.json())

def handle_code_request(user_request):
    code = generate_code(user_request)
    if code:
        save_code_to_github(code)        
        explanation = f"I have generated code and saved it to your GitHub repository as 'generated_code_{int(time.time())}.py'."
        audio_file_path = generate_speech(explanation)
        if audio_file_path:
            play_audio(audio_file_path)