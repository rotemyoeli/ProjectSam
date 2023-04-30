import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


def analyze_sentiment(text):
    # nltk.download('vader_lexicon')  # Download the sentiment analyzer lexicon
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)['compound']
    sentiment = 'positive' if score > 0 else 'negative'
    return round(score, 2), sentiment