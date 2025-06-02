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


def sentiment_analysis(tokenized_text):

    with open("master_dict/positive-words.txt", "r") as f:
        positive_words = set(f.read().splitlines())
    with open("master_dict/negative-words.txt", "r", encoding="utf-8", errors="replace") as f:
        negative_words = set(f.read().splitlines())
    
    positive_score = 0
    negative_score = 0

    for word in tokenized_text:
        if word.lower() in positive_words:
            positive_score += 1
        elif word.lower() in negative_words:
            negative_score += 1


    polarity_score = (positive_score - negative_score)/(positive_score + negative_score + 0.000001)

    subjectivity_score = (positive_score + negative_score)/(len(tokenized_text) + 0.000001)

    return positive_score, negative_score, polarity_score, subjectivity_score


def count_syllables(word):
    word = word.lower()
    count = 0
    vowels = 'aeiouy'
    

    if word.endswith('es') or word.endswith('ed'):

        word = word[:-2]

    prev_char_is_vowel = False
    for char in word:

        is_vowel = char in vowels
        if is_vowel and not prev_char_is_vowel:
            count += 1
        prev_char_is_vowel = is_vowel
        
    if count == 0:
        count = 1
    return count

def complex_word_count(words):
    return sum(1 for word in words if count_syllables(word) > 2)

def readability_analysis(article, total_words):

    sentences = sent_tokenize(article)

    
    avg_sent_length = len(total_words)/len(sentences)

    num_of_complex_words = complex_word_count(total_words)

    percentage_of_complex_words = (num_of_complex_words/len(total_words))*100

    fog_index = 0.4 * (avg_sent_length + percentage_of_complex_words)

    return avg_sent_length, percentage_of_complex_words, fog_index


def cleaned_word_count(words):

    stop_words = set(stopwords.words('english'))

    cleaned_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    return len(cleaned_words)


def count_personal_pronouns(words):

    pronouns_set = {"i", "we", "my", "ours", "us"}
    
    return sum(1 for word in words if word.lower() in pronouns_set and word != "US")


if __name__ == "__main__":
    extract_article("https://insights.blackcoffer.com/ai-and-ml-based-youtube-analytics-and-content-creation-tool-for-optimizing-subscriber-engagement-and-content-strategy/")