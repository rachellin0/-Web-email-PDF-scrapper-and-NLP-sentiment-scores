

# !pip install vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import pandas as pd
import re
import spacy
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import pandas as pd

# Download necessary resources
nltk.download('punkt')
nltk.download('stopwords')


class SentimentScorer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def score_sentiment(self, text):
        sentiment_scores = self.analyzer.polarity_scores(text)
        return sentiment_scores['compound']

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        self.nlp = spacy.load("en_core_web_sm")

    def clean_text(self, text):
        clean_text = text.replace("\n", " ").replace("/", " ")
        clean_text = ''.join([c for c in clean_text if c != "'"])
        return clean_text

    def split_into_sentences(self, text):
        doc = self.nlp(text)
        sentences = [sent.text.strip() for sent in doc.sents]
        return sentences

    def get_vader_sentiment(self, text):
        sentiment_scores = self.analyzer.polarity_scores(text)
        return sentiment_scores['compound']

    def get_textblob_sentiment(self, text):
        txt = TextBlob(text)
        polarity = txt.sentiment.polarity
        subjectivity = txt.sentiment.subjectivity
        return polarity, subjectivity

    def analyze_text(self, text_object):
        text = text_object.text  # Extract the text from TextObject
        # Handle text that's too long for spaCy
        if len(text) > self.nlp.max_length:
            text = text[:self.nlp.max_length]

        cleaned_text = self.clean_text(text)
        sentences = self.split_into_sentences(cleaned_text)

        vader_sentiments = []
        textblob_sentiments = []

        for sentence in sentences:
            vader_score = self.get_vader_sentiment(sentence)
            textblob_polarity, textblob_subjectivity = self.get_textblob_sentiment(sentence)

            vader_sentiments.append(vader_score)
            textblob_sentiments.append((textblob_polarity, textblob_subjectivity))

        sentiment_df = pd.DataFrame({
            'Sentence': sentences,
            'Vader_Sentiment': vader_sentiments,
            'TextBlob_Polarity': [item[0] for item in textblob_sentiments],
            'TextBlob_Subjectivity': [item[1] for item in textblob_sentiments]
        })

        return sentiment_df


