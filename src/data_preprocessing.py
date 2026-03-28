import pandas as pd
import re

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

def load_and_prepare_data(path):
    df = pd.read_csv(
        path,
        header=None,
        names=['sentiment_label', 'headline'],
        encoding='latin1'
    )

    # Normalize labels
    df['sentiment_label'] = df['sentiment_label'].str.strip().str.lower().str.capitalize()

    # Add date column for downstream analysis
    df['date'] = pd.date_range(start='2025-01-01', periods=len(df))

    # Clean text
    df['clean_headline'] = df['headline'].apply(clean_text)

    return df