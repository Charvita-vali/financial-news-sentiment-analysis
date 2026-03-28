# 📊 Financial News Sentiment Analysis

An end-to-end Natural Language Processing (NLP) project that analyzes financial news sentiment and explores its relationship with market trends.

---

## 🚀 Overview

This project builds a machine learning pipeline to classify financial news into **Positive, Negative, and Neutral sentiment**, and analyzes how sentiment signals relate to stock market behavior.

---

## 💼 Business Problem

Financial markets are influenced not only by numerical data but also by **news sentiment**.  
This project demonstrates how unstructured text data can be transformed into actionable insights for market analysis.

---

## ⚙️ Tech Stack

- Python  
- Pandas & NumPy  
- Scikit-learn  
- Matplotlib  
- yFinance  
- NLP (TF-IDF, text preprocessing)

---

## 🔄 Project Workflow

1. Load financial news dataset  
2. Clean and preprocess text  
3. Convert text into features (TF-IDF)  
4. Train ML model (Logistic Regression)  
5. Evaluate model performance  
6. Generate sentiment scores  
7. Analyze sentiment vs market trends  
8. Visualize results  

---

## 📂 Project Structure

financial-news-sentiment-analysis/
│
├── data/
│ ├── real_financial_news.csv
│ └── sample_financial_news.csv
│
├── notebooks/
│ └── analysis.ipynb
│
├── outputs/
│ ├── sentiment_distribution_linkedin.png
│ ├── sentiment_vs_return.png
│ └── market_trend.png
│
├── src/
│ ├── data_preprocessing.py
│ ├── sentiment_model.py
│ ├── market_analysis.py
│ └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore

## ▶️ How to Run

```bash
git clone https://github.com/Charvita-vali/financial-news-sentiment-analysis
cd financial-news-sentiment-analysis

>>>>>>> 36f0ea8 (Improved project to professional level (README, structure, documentation))
pip install -r requirements.txt

python src/main.py

## 📊 Visualization

![Sentiment vs Market Return](outputs/sentiment_vs_return.png)

## 📈 Results

- Model Accuracy: ~72%
- Successfully classified financial news sentiment
- Observed correlation patterns between sentiment and market returns
- Generated insights useful for financial decision-making

📊 Results
Model Accuracy: ~72%
Successfully classified financial news sentiment
Generated insights from unstructured text data

📈 Visualizations

🔹 Sentiment Distribution
🔹 Sentiment vs Market Returns
🔹 Market Trend

⚠️ Limitations

Dataset dates are synthetic/generated
Market correlation is illustrative, not predictive
Model performance can be improved with advanced NLP models

🚀 Future Improvements

Use deep learning models (LSTM, BERT)
Add real-time news data pipeline
Deploy as a web application
Improve feature engineering

🎯 Key Takeaways

NLP can extract insights from unstructured financial data
Feature engineering plays a critical role in model performance
Sentiment analysis can support data-driven financial decisions

🔗 Author
Charvita Vali

