import requests
from jarvis_assistant import *
from local_keys import *  


def get_weather():
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={WEATHER_CITY}&aqi=no")
    if response.status_code == 200:
        weather_data = response.json()
        temperature_f = weather_data['current']['temp_f']
        condition = weather_data['current']['condition']['text']
        return f"The current temperature in {WEATHER_CITY} is {temperature_f} degrees Fahrenheit with a {condition} condition."
    else:
        return "I couldn't fetch the weather information at the moment."

def handle_weather_command():
    weather_report = get_weather()
    print("JARVIS:", weather_report)

    audio_file_path = generate_speech(weather_report)
    if audio_file_path:
        print(f"Playing weather report: {audio_file_path}")
        play_audio(audio_file_path)