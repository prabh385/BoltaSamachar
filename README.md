It is a web application that scrapes news articles concerning a specified company, does sentiment analysis, and provides a text-to-speech (TTS) response in Hindi. The app accepts a company name as input and delivers an organized sentiment report and an audio summary.

Features

News Extraction: Retrieves and shows major information from a minimum of 10 different news articles with the help of web scraping (BeautifulSoup).

Sentiment Analysis: Examines article sentiment (positive, negative, neutral) with the use of a pre-trained NLP model.

Comparative Analysis: Compares sentiment scores to show overall media outlook.

Text-to-Speech (TTS): Translates summary content to Hindi speech utilizing an open-source TTS model.

User Interface: Offers interactive frontend through Streamlit or Gradio.

API-Based Communication: Maintains data sharing between frontend and backend in smooth communication.

Deployment: Deployed on Hugging Face Spaces to ensure ready availability.