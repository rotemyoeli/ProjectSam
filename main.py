import GetSentiment
import SiteScreen
import openai

# text = "On the hunt for new hiking shoes? In 10 years, our all-female hiking team has tested 50 pairs, with the 12 best contenders now available in our current review. Our hiking enthusiasts have done leg work, busting out hundreds of long miles over the years through deserts, forests, mountains, and streams. We carry loaded packs, consider all-day comfort, and evaluate traction over and through wet, loose, and slippery surfaces. From differing foot shapes to varied trail conditions, we look at it all and rank each shoe according to our on-trail experiences. Over months of side-by-side comparison and testing, we tease apart the differences between these shoes and share our findings to help you pinpoint your perfect pair. Hiking is a world of fun in which you can either load up on gear or head out with nothing more than a stellar hydration pack and a good pair of shoes. But if you are the kind of hiker that loves to have all the top-notch hiking gear, we've probably tested it and have recommendations for you. If you are planning longer treks, carrying a heavy pack, or just prefer to have a bit more support, you might be interested in women's high-top hiking boots. If you're looking for men's hiking shoes, we've tested those too."

url = "https://www.switchbacktravel.com/best-tents-backpacking"
paragraphs = SiteScreen.get_text(url)
# paragraphs = SiteScreen.get_paragraphs("https://www.outravel.co.il/")

totalScore = 0
counter = 0
texts = ["Big Agnes Copper", "Nemo Kunai", "Salomon Outward Mid GTX"]

# Loop through each paragraph and print the sentiment score
for paragraph in paragraphs:
    counter = counter+1
    score, sentiment = GetSentiment.analyze_sentiment(paragraph)
    totalScore = (totalScore + score) / counter
    for text in texts:
        if text in paragraph:
            print(f"Sentiment score: {score}\nSentiment: {sentiment}\nText: {paragraph}")

