import requests
from jarvis_assistant import generate_speech, play_audio
from local_keys import NEWS_API_KEY

def get_news(api_key=NEWS_API_KEY, country='us', category=None, query=None):
    """Fetch top news headlines based on country, category, or search query."""
    base_url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': country,
        'category': category,
        'q': query,
        'apiKey': api_key
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        news_data = response.json()
        if news_data['status'] == 'ok':
            articles = news_data['articles']
            return articles
        else:
            print("Error in API response:", news_data.get('message'))
    else:
        print(f"Error: {response.status_code}")

def handle_news_command(category=None, query=None):
    """Handle the 'news' command to fetch and speak out the news headlines."""
    articles = get_news(category=category, query=query)
    if articles:
        news_summary = "Here are the top headlines: "
        for article in articles[:5]: 
            news_summary += f"{article['title']}. "
        print("JARVIS:", news_summary)

        audio_file_path = generate_speech(news_summary)
        if audio_file_path:
            play_audio(audio_file_path)
    else:
        error_message = "I'm sorry, I couldn't fetch the news right now."
        print("JARVIS:", error_message)
        
        audio_file_path = generate_speech(error_message)
        if audio_file_path:
            play_audio(audio_file_path)
