"""
Machine learning model for sentiment classification.
"""
from typing import Tuple
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib


def train_sentiment_model(df: pd.DataFrame) -> Tuple[Pipeline, dict]:
    X = df['clean_headline']
    y = df['sentiment_label']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.4, random_state=42, stratify=y
    )

    model = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english', ngram_range=(1, 2))),
        ('clf', LogisticRegression(max_iter=1000))
    ])

    model.fit(X_train, y_train)
    joblib.dump(model, "outputs/model.joblib")
    preds = model.predict(X_test)

    metrics = {
        'accuracy': accuracy_score(y_test, preds),
        'report': classification_report(y_test, preds, output_dict=False)
    }
    return model, metrics

def score_sentiment(model: Pipeline, texts):
    return model.predict(texts)
