from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
from transformers import pipeline
from gtts import gTTS
import os

# Initialize FastAPI app
app = FastAPI(title="BoltaSamachar API")

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

class NewsRequest(BaseModel):
    company: str

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

@app.post("/get_news")
def get_news(data: NewsRequest):
    articles = fetch_news(data.company)
    if not articles:
        raise HTTPException(status_code=404, detail="No news found")
    return {"articles": articles}

@app.post("/analyze_sentiment")
def get_sentiment(data: NewsRequest):
    articles = fetch_news(data.company)
    analyzed_articles = analyze_sentiment(articles)
    return {"articles": analyzed_articles}

@app.post("/generate_tts")
def generate_tts(data: NewsRequest):
    text = f"Here is a summary of news for {data.company}"
    file_path = text_to_speech(text)
    return {"audio_file": file_path}
