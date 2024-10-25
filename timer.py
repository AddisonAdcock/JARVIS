import time
import re
from jarvis_assistant import generate_speech, play_audio

timers = []

def set_timer(duration):
    """Set a timer for the given duration in seconds."""
    timestamp = time.time() + duration
    timers.append(timestamp)
    timer_message = f"Timer set for {duration} seconds."
    print(timer_message)

    audio_file_path = generate_speech(timer_message)
    if audio_file_path:
        play_audio(audio_file_path)

def check_timers():
    current_time = time.time()
    for timestamp in timers[:]:
        if current_time >= timestamp:
            alarm_sound()
            timers.remove(timestamp)

def alarm_sound():
    alarm_message = "Time's up!"
    print(alarm_message)

    audio_file_path = generate_speech(alarm_message)
    if audio_file_path:
        print(f"Playing alarm: {audio_file_path}")
        play_audio(audio_file_path)

def handle_timer_command(duration):
    try:
        total_seconds = parse_duration(duration)

        if total_seconds is not None:
            set_timer(total_seconds)
        else:
            raise ValueError("Unable to parse the duration")
        
    except ValueError:
        print("Sorry, I couldn't understand the timer duration. Please specify in seconds, minutes, or hours.")
        audio_file_path = generate_speech("Sorry, I couldn't understand the timer duration. Please specify in seconds, minutes, or hours.")
        if audio_file_path:
            play_audio(audio_file_path)

def parse_duration(duration):
    """Parse the duration string and return total seconds."""
    total_seconds = 0
    duration = duration.lower().strip()

    hour_match = re.findall(r'(\d+)\s*hour', duration)
    minute_match = re.findall(r'(\d+)\s*minute', duration)
    second_match = re.findall(r'(\d+)\s*second', duration)

    if hour_match:
        total_seconds += sum(int(hour) * 3600 for hour in hour_match)

    if minute_match:
        total_seconds += sum(int(minute) * 60 for minute in minute_match)

    if second_match:
        total_seconds += sum(int(second) for second in second_match)

    return total_seconds if total_seconds > 0 else None
