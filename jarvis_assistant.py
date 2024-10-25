import subprocess
import os
import json
from pathlib import Path
import time
import pygame
import speech_recognition as sr
from local_keys import * 


messages = [{"role": "system", "content": (
        "You are JARVIS from the Ironman movies. I am not Tony Stark, but I am your commander. "
        "You are a helpful and comical assistant and all of your responses will be read out loud "
        "so make sure they sound as if they should be spoken. Keep your responses a reasonable length "
        "(not overly long unless you think it is required). I am to be called 'Sir'."
    )}]

def generate_speech(text, voice="echo"):
    audio_dir = Path(__file__).parent / "audio"
    audio_dir.mkdir(exist_ok=True)
    timestamp = int(time.time())
    speech_file_path = audio_dir / f"speech_{timestamp}.mp3"
    
    if speech_file_path.exists():
        try:
            speech_file_path.unlink()
        except Exception as e:
            print(f"Error deleting existing file: {e}")

    curl_command = [
        "curl", "https://api.openai.com/v1/audio/speech",
        "-H", "Content-Type: application/json",
        "-H", f"Authorization: Bearer {API_KEY}",
        "-d", json.dumps({
            "model": "tts-1",
            "voice": voice,
            "input": text
        }),
        "--output", str(speech_file_path)
    ]
    
    try:
        subprocess.run(curl_command, check=True)
        return speech_file_path
    except subprocess.CalledProcessError as e:
        print(f"Error generating audio: {e.stderr}")
        return None

def chat_with_gpt(messages):
    curl_command = [
        "curl", "https://api.openai.com/v1/chat/completions",
        "-H", "Content-Type: application/json",
        "-H", f"Authorization: Bearer {API_KEY}",
        "-d", json.dumps({
            "model": "gpt-3.5-turbo",
            "messages": messages,
            "max_tokens": 150,
            "temperature": 0.7
        })
    ]
    try:
        result = subprocess.run(curl_command, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return None

def listen_for_jarvis():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    
    with mic as source:
        print("Listening for 'Jarvis'...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        if "jarvis" in command:
            return command
        else:
            print("No 'Jarvis' detected in speech.")
            return None
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return None

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def handle_user_command(user_command):
    messages.append({"role": "user", "content": user_command})
    response = chat_with_gpt(messages)

    if response:
        assistant_reply = response['choices'][0]['message']['content']
        print("JARVIS:", assistant_reply)

        audio_file_path = generate_speech(assistant_reply)
        if audio_file_path:
            print(f"Playing response: {audio_file_path}")
            play_audio(audio_file_path)

        messages.append({"role": "assistant", "content": assistant_reply})
