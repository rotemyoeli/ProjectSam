import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)['compound']
    sentiment = 'positive' if score > 0 else 'negative'
    return round(score * 10, 2), sentiment