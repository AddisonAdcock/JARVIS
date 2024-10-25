from datetime import datetime
from jarvis_assistant import *

def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    return f"The current time is {current_time}."

def handle_time_command():
    time_report = get_current_time()
    print("JARVIS:", time_report)

    audio_file_path = generate_speech(time_report)
    if audio_file_path:
        print(f"Playing time report: {audio_file_path}")
        play_audio(audio_file_path)
