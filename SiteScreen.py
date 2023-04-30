import requests
from bs4 import BeautifulSoup


# Set the URL of the website to scrape
# url = 'https://www.cnn.com/business'
def get_text(url):
    # Send a GET request to the website and get its HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the paragraphs on the page and store them in a list
    paragraphs = [p.text.strip() for p in soup.find_all('p')]
    return paragraphs