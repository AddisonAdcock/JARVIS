# JARVIS Assistant

Welcome to the JARVIS Assistant project! JARVIS is a voice-activated assistant inspired by the AI from Iron Man, designed to help you with a wide range of tasks. This project leverages various APIs to provide functionalities such as weather updates, timer management, code generation, news fetching, and more. Powered by Open AI's TTS, GPT 3.5 Turbo, and GPT 4.

## Features

- Voice Commands: Interact with JARVIS using natural language voice commands.
- Weather Updates: Get current weather information for any location.
- Timer Management: Set and manage timers for various tasks.
- Code Generation: Generate Python code snippets based on user requests.
- Current Time: Retrieve the current time in a specified format.
- News Fetching: Stay updated with the latest news headlines.
- Play Spotify: Play a song through spotify on the web.

## Getting Started

To get started with JARVIS Assistant, follow these steps:

### Prerequisites

Make sure you have the following installed:

- Python 3.7 or later
- `pip` for managing Python packages

### Clone the Repository

git clone <repository-url> cd <repository-directory>

### Install Required Packages

Install the necessary Python libraries:

- base64
- datetime
- json
- os
- pathlib
- pyautogui
- pygame
- re
- requests
- speech_recognition
- subprocess
- time
- webbrowser

### Setting Up API Keys

You will need several API keys for the JARVIS Assistant to function properly. Create a file named `local_keys.py` in the project directory and add the following keys:


- API_KEY = "your_openai_api_key"

- WEATHER_API_KEY = "your_weather_api_key"
- WEATHER_URL = "http://api.weatherapi.com/v1/current.json"
- WEATHER_CITY = "your_default_city"

- NEWS_API_KEY = "your_news_api_key"


# Obtaining API Keys
OpenAI API Key: Sign up at OpenAI to obtain an API key.
Weather API Key: Register at WeatherAPI to get your API key.
News API Key: Get an API key from NewsAPI.

# Running the Assistant
Once you have added your API keys, you can run the JARVIS Assistant using "python main.py"

# Contribution
Feel free to fork this repository and make improvements!





