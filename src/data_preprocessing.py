import re
import pandas as pd

def clean_text(text: str) -> str:
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def load_and_prepare_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df['clean_headline'] = df['headline'].apply(clean_text)
    return df
