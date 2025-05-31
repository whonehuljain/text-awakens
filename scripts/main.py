import pandas as pd
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import re
import os
from nltk.corpus import stopwords

nltk.download('punkt_tab')
nltk.download('stopwords')

def extract_article(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # title
        title = soup.find('h1').text.strip() if soup.find('h1') else ''
        
        # article content
        article = soup.find('article') or soup.find('div', class_='post-content')
        if article:

            for element in article.find_all(['script', 'style', 'nav', 'header', 'footer']):
                element.decompose()
                
            text = title + '\n\n' + article.get_text(strip=True)
            return text
        return None
    except Exception as e:
        print(f"Error extracting article from {url}: {str(e)}")
        return None
    
def preprocess_text(text):

    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    

    text = re.sub(r'(\d+)([A-Za-z])', r'\1 \2', text)
    text = re.sub(r'([A-Za-z])(\d+)', r'\1 \2', text)

    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)  # camelCase
    text = re.sub(r'([A-Z])([A-Z][a-z])', r'\1 \2', text)  # PascalCase

    text = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', text)

    text = re.sub(r'(\d+)([A-Za-z])', r'\1 \2', text)
    text = re.sub(r'([A-Za-z])(\d+)', r'\1 \2', text)


    
    return text


def get_tokenized_words(text):
    text = preprocess_text(text)
    words = word_tokenize(text)
    return words


def remove_stopwords(words):

    stopwords_set = set()
    for filename in os.listdir("stopwords"):
        filepath = os.path.join("stopwords", filename)
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            stopwords_set.update(word.lower() for word in f.read().splitlines())
    
    cleaned_words = [word.lower() for word in words if word.lower() not in stopwords_set]
    return cleaned_words


if __name__ == "__main__":
    extract_article("https://insights.blackcoffer.com/ai-and-ml-based-youtube-analytics-and-content-creation-tool-for-optimizing-subscriber-engagement-and-content-strategy/")