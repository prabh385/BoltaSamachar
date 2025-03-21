import requests
from bs4 import BeautifulSoup
from transformers import pipeline
from gtts import gTTS

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def fetch_news(company):
    url = f"https://news.google.com/search?q={company}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = []
    for item in soup.find_all("h3")[:10]:
        title = item.text
        link = item.find("a")["href"] if item.find("a") else ""
        articles.append({"title": title, "link": link})
    return articles

def analyze_sentiment(articles):
    for article in articles:
        sentiment = sentiment_pipeline(article["title"])[0]
        article["sentiment"] = sentiment["label"]
    return articles

def text_to_speech(text):
    tts = gTTS(text=text, lang='hi')
    file_path = "output.mp3"
    tts.save(file_path)
    return file_path
