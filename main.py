import GetSentiment


text = "I absolutely loved the movie! The acting was superb and the plot kept me engaged throughout."
score, sentiment = GetSentiment.analyze_sentiment(text)
print(f"Sentiment score: {score}\nSentiment: {sentiment}")