import GetSentiment
import SiteScreen
import openai

import tkinter as tk
from tkinter import scrolledtext
from functools import partial
import clipboard

#new

def add_url(urls, url_entry):
    # Get the text from the clipboard
    clipboard_text = clipboard.paste()

    # If there is text in the clipboard, insert it into the URL entry field
    if clipboard_text:
        url_entry.insert(tk.END, clipboard_text)

    # Add the URL to the set of URLs and clear the entry field
    urls.add(url_entry.get())
    url_entry.delete(0, tk.END)
    url_entry.focus()

    # Update the clipboard with the URL that was added
    clipboard.copy(url_entry.get())

def process_urls(urls, output_text):
    # Placeholder function that processes the URLs
    output_text.insert(tk.END, "Processing URLs: " + str(urls) + "\n")

def process_text(text, output_text):
    # Placeholder function that processes the text
    output_text.insert(tk.END, "Processing text: " + str(texts) + "\n")


def add_text(texts, text_entry):
    # Get the text from the clipboard
    clipboard_text = clipboard.paste()

    # If there is text in the clipboard, insert it into the text entry field
    if clipboard_text:
        text_entry.insert(tk.END, clipboard_text)

    # Add the URL to the set of URLs and clear the entry field
    texts.add(text_entry.get())
    text_entry.delete(1, tk.END)
    text_entry.focus()

    # Update the clipboard with the URL that was added
    clipboard.copy(text_entry.get())


# Create the GUI window
window = tk.Tk()
window.title("Website and Text Processor")

# Create a set to store the URLs and a set to store the texts
urls = set()
texts = set()

# Create a text area to display the output
output_text = scrolledtext.ScrolledText(window, width=40, height=10)
output_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Create a label and entry field for adding URLs
url_label = tk.Label(window, text="Add URL:")
url_label.grid(row=0, column=0, padx=5, pady=5)
url_entry = tk.Entry(window, width=30, exportselection=0, selectbackground="light blue")
url_entry.grid(row=0, column=1, padx=5, pady=5)
url_button = tk.Button(window, text="Add", command=partial(add_url, urls, url_entry))
url_button.grid(row=0, column=2, padx=5, pady=5)

# Create a label and entry field for adding text
text_label = tk.Label(window, text="Add text:")
text_label.grid(row=1, column=0, padx=5, pady=5)
text_entry = tk.Entry(window, width=30, exportselection=0, selectbackground="light blue")
text_entry.grid(row=1, column=1, padx=5, pady=5)
text_button = tk.Button(window, text="Add", command=partial(add_text, texts, text_entry))
text_button.grid(row=1, column=2, padx=5, pady=5)

# Create a button to process the URLs and texts
process_button = tk.Button(window, text="Process", command=lambda: [process_urls(urls, output_text), process_text(texts.pop(), output_text)])
process_button.grid(row=2, column=1, padx=5, pady=5)

# Start the GUI event loop
window.mainloop()




'''
url = "https://www.rei.com/learn/expert-advice/best-approach-shoes.html"
#paragraphs = SiteScreen.scrape_website_text(url)

paragraphs = SiteScreen.download_chapters(url)
# paragraphs = SiteScreen.get_paragraphs(url)

totalScore = 0
counter = 0
texts = ["Big Agnes Copper", "Zpacks Duplex", "Nemo Dagger"]

# Loop through each paragraph and print the sentiment score
for paragraph in paragraphs:
    counter = counter+1
    score, sentiment = GetSentiment.analyze_sentiment(paragraph)
    #totalScore = (totalScore + score) / counter
    if score > 0.5:
        print(f"Sentiment score: {score}\nSentiment: {sentiment}\nText: {paragraph}")

    for text in texts:
        if text in paragraph:
            print(f"Sentiment score: {score}\nSentiment: {sentiment}\nText: {paragraph}")

'''