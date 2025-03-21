from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.utils import fetch_news, analyze_sentiment, text_to_speech

router = APIRouter()

class NewsRequest(BaseModel):
    company: str

@router.post("/get_news")
def get_news(data: NewsRequest):
    articles = fetch_news(data.company)
    if not articles:
        raise HTTPException(status_code=404, detail="No news found")
    return {"articles": articles}

@router.post("/analyze_sentiment")
def get_sentiment(data: NewsRequest):
    articles = fetch_news(data.company)
    analyzed_articles = analyze_sentiment(articles)
    return {"articles": analyzed_articles}

@router.post("/generate_tts")
def generate_tts(data: NewsRequest):
    text = f"Here is a summary of news for {data.company}"
    file_path = text_to_speech(text)
    return {"audio_file": file_path}