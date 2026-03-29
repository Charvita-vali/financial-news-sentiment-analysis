# 📊 Financial News Sentiment Analysis

An end-to-end Natural Language Processing (NLP) project that analyzes financial news sentiment and explores its relationship with stock market trends.

---

## 🚀 Project Highlights

* Built a complete NLP pipeline for sentiment classification
* Used TF-IDF and Logistic Regression for modeling
* Integrated real market data using yFinance
* Achieved ~72% model accuracy
* Visualized sentiment trends vs stock market performance

---

## 🧠 Problem Statement

Financial markets are influenced not only by numerical data but also by news sentiment.
This project demonstrates how unstructured text data can be transformed into actionable insights for market analysis.

---

## ⚙️ How It Works

1. Load financial news dataset
2. Clean and preprocess text data
3. Convert text into TF-IDF features
4. Train Logistic Regression model
5. Generate sentiment scores
6. Merge with stock market data (S&P 500)
7. Visualize trends and insights

---

## 🛠 Tech Stack

* Python
* Pandas & NumPy
* Scikit-learn
* Matplotlib
* yFinance
* NLP (TF-IDF, text preprocessing)

---

## 📁 Project Structure

financial-news-sentiment-analysis/
│── data/
│   ├── real_financial_news.csv
│   ├── sample_financial_news.csv
│
│── notebooks/
│   └── analysis.ipynb
│
│── outputs/
│   ├── sentiment_distribution.png
│   ├── sentiment_vs_return.png
│   ├── market_trend.png
│
│── src/
│   ├── data_preprocessing.py
│   ├── sentiment_model.py
│   ├── market_analysis.py
│   └── main.py
│
│── requirements.txt
│── README.md

---

## ▶️ How to Run

git clone https://github.com/Charvita-vali/financial-news-sentiment-analysis
cd financial-news-sentiment-analysis

pip install -r requirements.txt

python src/main.py

---

## 📈 Results

* Model Accuracy: ~72%
* Successfully classified financial news sentiment
* Identified patterns between sentiment and market movements
* Generated insights from unstructured financial data

---

## 📊 Visualizations

### Sentiment vs Market Return

![Sentiment vs Market Return](outputs/sentiment_vs_return.png)

---

## ⚠️ Limitations

* Dataset is partially synthetic / limited
* Market correlation is illustrative, not predictive
* Model performance can improve with advanced NLP techniques

---

## 🔮 Future Improvements

* Implement deep learning models (LSTM, BERT)
* Use real-time news APIs
* Deploy as a web application
* Improve feature engineering

---

## 👤 Author

**Charvita Vali**
