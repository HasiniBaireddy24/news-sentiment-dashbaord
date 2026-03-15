import requests
import pandas as pd

API_KEY = "YOUR_API_KEY"

def fetch_news(query="technology"):
    url = f"https://newsapi.org/v2/everything?q={query}&language=en&apiKey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    articles = data["articles"]

    news_data = []

    for article in articles:
        news_data.append({
            "title": article["title"],
            "description": article["description"],
            "source": article["source"]["name"],
            "publishedAt": article["publishedAt"]
        })

    df = pd.DataFrame(news_data)

    return df