from tkinter import *
from selenium import webdriver
import urllib.request
from selenium.webdriver.common.by import By
import GetSentiment
def download_website():
    driver = webdriver.Chrome()
    driver.get(url_entry.get())
    result = []
    text_box.delete(1.0, END)

    paragraphs = driver.find_elements(By.CSS_SELECTOR, "p")
    for paragraph in paragraphs:
        score, sentiment = GetSentiment.analyze_sentiment(paragraph.text)
        if score > 0.1:
            temp = paragraph.text + str(score) + sentiment
            result.append(temp)
            # text_box.insert(END, paragraph.text)
            # text_box.insert(END, score)
    # text = [paragraph.text for paragraph in paragraphs]

    '''
    images = driver.find_elements(By.CSS_SELECTOR, "img")
    for i, image in enumerate(images):
        image_url = image.get_attribute("src")
        urllib.request.urlretrieve(image_url, f"image_{i}.jpg")
    '''

    text_box.delete(1.0, END)
    text_box.insert(END, result)

    driver.quit()

root = Tk()
root.title("Web Text Downloader")

url_label = Label(root, text="URL:")
url_label.grid(row=0, column=0)

url_entry = Entry(root)
url_entry.grid(row=0, column=1)

download_button = Button(root, text="Download Website", command=download_website)
download_button.grid(row=1, column=0)

text_box = Text(root)
text_box.grid(row=2, column=0, columnspan=2)

root.mainloop()