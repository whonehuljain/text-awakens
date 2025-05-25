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
    


if __name__ == "__main__":
    extract_article("https://insights.blackcoffer.com/ai-and-ml-based-youtube-analytics-and-content-creation-tool-for-optimizing-subscriber-engagement-and-content-strategy/")