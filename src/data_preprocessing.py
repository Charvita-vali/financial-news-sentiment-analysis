"""
Data preprocessing module for financial news sentiment analysis.
Handles loading, cleaning, and preparing text data.
"""
import pandas as pd
import re

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

def load_and_prepare_data(path):
    """
    Load and preprocess financial news dataset.

    Args:
        path (str): Path to CSV file

    Returns:
        pd.DataFrame: Cleaned dataset
    """
    df = pd.read_csv(path, header=None, encoding='latin1')

    df.columns = ['sentiment_label', 'headline']

    df['sentiment_label'] = df['sentiment_label'].str.capitalize()

    df['date'] = pd.date_range(start='2025-01-01', periods=len(df))

    df['clean_headline'] = df['headline'].apply(clean_text)

    return df