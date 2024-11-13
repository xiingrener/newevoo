import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import nltk # toinstall
from textblob import TextBlob

nltk.download("punkt")
nltk.download("stopwords")

data = pd.read_csv("qualitative.csv")
'''
seq = 1
prec = 1
rev = 1
data = data[(data['con.sequence'] == seq) & (data['con.precise'] == prec) & (data['con.reveal'] == rev)]
'''
data = data[(data['con.reveal'] == 1)]

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

sentiment_results = data['bestTip'].dropna().apply(analyze_sentiment)

data.loc[data['bestTip'].notnull(), 'sentiment_polarity'] = [result[0] for result in sentiment_results]
data.loc[data['bestTip'].notnull(), 'sentiment_subjectivity'] = [result[1] for result in sentiment_results]

data_sentiment_with_bonus = data[['bestTip', 'sentiment_polarity', 'sentiment_subjectivity', 'rationaleFeeling', 'total_bonus', 'con.sequence', 'con.precise', 'con.reveal']]

print(data_sentiment_with_bonus.head())

# Save the sentiment analysis results with bonus to a CSV file
#chu = f"{seq}{prec}{rev}qual.csv"
chu = "sent.csv"
data_sentiment_with_bonus.to_csv(chu, index=False)
