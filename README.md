# Sentiment & Readability Analysis Tool

## Project Overview
This project is a Python-based tool that automates the extraction, sentiment analysis, and readability assessment of web articles. It fetches article content, processes the text, computes sentiment and readability metrics, and outputs results in a structured format for easy analysis.

---

## Features

- **Web Content Extraction:** Fetches and cleans article text, removing scripts, styles, and navigation bars.
- **Sentiment Analysis:** 
  - Uses custom stopword lists and positive/negative word dictionaries.
  - Calculates positive/negative scores, polarity, and subjectivity.
- **Readability Analysis:** 
  - Computes average sentence length, complex word percentage, Fog Index, and syllables per word.
- **Automated Reporting:** Saves cleaned articles and generates an Excel report with all metrics.

---

## Installation

1. **Python Requirement:** Ensure Python 3.7 or above is installed.
2. **Install Dependencies:**
    ```
    pip install -r requirements.txt
    ```
3. **Folder Structure:**  
    Ensure your project directory looks like this:
    ```
    project-folder/
    ├── data/
    │   └── Input.xlsx
    ├── master_dict/
    │   ├── positive-words.txt
    │   └── negative-words.txt
    ├── scripts/
    │   └── main.py
    ├── stopwords/
    │   └── (stopword files)
    └── output/
        └── (created automatically)
    ```

---

## Usage

1. **Prepare Input:** Add URLs to `data/Input.xlsx`.
2. **Run the Script:**  
    Navigate to the `scripts/` directory and execute:
    ```
    python3 main.py
    ```
3. **View Output:**  
    - Extracted article text: `output/article_text/`
    - Analysis results: `output/Output.xlsx`

---

## Metrics Calculated

| Metric              | Description                                   |
|---------------------|-----------------------------------------------|
| Positive Score      | % of positive words in the article            |
| Negative Score      | % of negative words in the article            |
| Polarity            | Sentiment score (-1 to 1)                     |
| Subjectivity        | Opinion vs. fact ratio (0 to 1)               |
| Avg Sentence Length | Words per sentence                            |
| Complex Word %      | % of words with >2 syllables                  |
| Fog Index           | Readability difficulty score                  |
| Syllables/Word      | Average syllables per word                    |

---

## Dependencies

- `beautifulsoup4`
- `pandas`
- `openpyxl`
- `nltk`
- `requests`

---

## Troubleshooting

- **NLTK Errors:**  
    If you encounter NLTK-related errors, run:
    ```
    import nltk
    nltk.download('punkt')
    ```
- **Internet Access:**  
    Required for fetching articles.
- **Folder Errors:**  
    Ensure all folders and files match the required structure.

---

## Customization

- **Dictionaries:**  
    Edit `master_dict/positive-words.txt` and `negative-words.txt` to refine sentiment analysis.
- **Stopwords:**  
    Add or modify stopword files in the `stopwords/` directory.

---

## License

This project is for educational and research purposes.
