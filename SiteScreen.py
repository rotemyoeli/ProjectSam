import requests
from bs4 import BeautifulSoup

import re
import urllib.parse

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By

def download_chapters(url):
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()

    # Navigate to the website
    driver.get(url)

    # Find all the headings on the page and store them in an array
    headings = driver.find_elements(By.XPATH, "//h1 | //h2 | //h3 | //h4 | //h5 | //h6")

    # Find the text between each pair of headings and store it in an array of chapters
    chapters = []
    for i in range(len(headings) - 1):
        start = headings[i]
        end = headings[i + 1]
        text = ""
        current = start
        while current != end:
            try:
                current = current.find_element(By.XPATH, "following-sibling::*[not(self::h1 or self::h2 or self::h3 or self::h4 or self::h5 or self::h6)][1]")
                if current.tag_name == "p":
                    text += current.text + "\n\n"
            except:
                break
        chapters.append(text)

    # Close the browser
    driver.quit()

    # Return the array of chapters
    return chapters

def scrape_website_text(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    page_source = driver.execute_script('return document.body.innerHTML')
    soup = BeautifulSoup(page_source, 'html.parser')
    page_text = soup.get_text()
    driver.quit()
    return page_text





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
    counter = 0
    while queue and counter < 100:
        url = queue.pop(0)
        counter = counter + 1
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