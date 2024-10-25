from jarvis_assistant import *
from weather import *
from timer import *
from current_time import *
from code_generator import *
from news import *

def main():
    while True:
        user_command = listen_for_jarvis()
        if user_command:
            print(f"You said: {user_command}")
            if "code" in user_command:
                code_request = user_command.split("code")[-1].strip()
                handle_code_request(code_request)
            elif "weather" in user_command:
                handle_weather_command()
            elif "what" in user_command and "time" in user_command:
                handle_time_command()
            elif "set a timer" in user_command:
                duration = user_command.split("set a timer for")[-1].strip()
                handle_timer_command(duration)
            elif "news" in user_command:
                handle_news_command()
            else:
                handle_user_command(user_command)
        check_timers()

if __name__ == "__main__":
    main()
