# Financial News Sentiment Analysis & Market Insights

An end-to-end NLP project that classifies financial news sentiment and analyzes its relationship with stock market behavior.

## Project Overview

This project builds a complete data analytics pipeline that:

- Collects or ingests financial news headlines/articles  
- Cleans and preprocesses text data  
- Classifies sentiment as Positive, Negative, or Neutral  
- Aggregates sentiment trends over time  
- Joins sentiment outputs with stock market data  
- Generates insights for financial and news-based decision-making  

##  Business Problem

Financial markets react quickly to news sentiment. This project helps analysts understand whether sentiment trends in financial news align with market movements and can support:

- Investment decision-making  
- Risk analysis  
- Market trend forecasting  

##  Tech Stack

- **Programming:** Python  
- **Data Processing:** Pandas, NumPy  
- **NLP:** TF-IDF Vectorization  
- **Machine Learning:** Logistic Regression (Scikit-learn)  
- **Visualization:** Matplotlib  
- **Market Data API:** yFinance  
- **Version Control:** Git, GitHub  

##  Project Architecture

1. **Data Ingestion**  
   - Financial news dataset (Kaggle / sample dataset)

2. **Data Preprocessing**  
   - Text cleaning (lowercasing, removing special characters)  
   - Label normalization  

3. **Feature Engineering**  
   - TF-IDF vectorization  

4. **Model Training**  
   - Logistic Regression classifier  

5. **Evaluation**  
   - Accuracy, precision, recall  

6. **Market Data Integration**  
   - Fetch stock data using yFinance  

7. **Analysis**  
   - Correlate sentiment with daily market returns  

8. **Visualization**  
   - Sentiment vs Market Return graph  

##  Dataset

- A **sample dataset** is included for quick testing and reproducibility  
- A **real-world dataset** can be downloaded from Kaggle:  
  https://www.kaggle.com/datasets/ankurzing/sentiment-analysis-for-financial-news

## 📈 Results

- Model Accuracy: ~72%
- Successfully classified financial news sentiment
- Observed correlation patterns between sentiment and market returns
- Generated insights useful for financial decision-making


