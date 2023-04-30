import requests
from bs4 import BeautifulSoup

import re
import urllib.parse

def get_text(url):
    # Send a GET request to the website and get its HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the paragraphs on the page and store them in a list
    paragraphs = [p.text.strip() for p in soup.find_all('p')]
    return paragraphs

def get_paragraphs(site_url):
    paragraphs = []
    visited_urls = set()
    queue = [site_url]
    while queue:
        url = queue.pop(0)
        if url in visited_urls:
            continue
        visited_urls.add(url)
        try:
            response = requests.get(url)
            if response.status_code != 200:
                continue
            soup = BeautifulSoup(response.content, "html.parser")
            for p in soup.find_all('p'):
                paragraphs.append(p.text)
            for link in soup.find_all('a', href=True):
                href = link.get('href')
                if not href.startswith("http"):
                    href = urllib.parse.urljoin(site_url, href)
                if href not in visited_urls and href not in queue:
                    queue.append(href)
        except:
            continue
    return paragraphs