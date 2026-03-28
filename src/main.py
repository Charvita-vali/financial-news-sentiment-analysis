from pathlib import Path
import matplotlib.pyplot as plt

from data_preprocessing import load_and_prepare_data
from sentiment_model import train_sentiment_model
from market_analysis import build_daily_sentiment, fetch_market_data, merge_sentiment_with_market


def plot_sentiment_trend(daily_sentiment, output_dir):
    plt.figure(figsize=(10, 5))
    plt.plot(daily_sentiment['date'], daily_sentiment['avg_sentiment_score'], marker='o')
    plt.title('Daily Financial News Sentiment Trend')
    plt.xlabel('Date')
    plt.ylabel('Average Sentiment Score')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_dir / 'sentiment_trend.png')
    plt.show()


def plot_market_trend(merged, output_dir):
    plt.figure(figsize=(10, 5))
    plt.plot(merged['date'], merged['close'], marker='o')
    plt.title('Market Close Price Trend')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_dir / 'market_trend.png')
    plt.show()


def plot_sentiment_vs_return(merged, output_dir):
    clean_df = merged.dropna(subset=['daily_return'])
    plt.figure(figsize=(10, 5))
    plt.scatter(clean_df['avg_sentiment_score'], clean_df['daily_return'])
    plt.title('Sentiment Score vs Daily Market Return')
    plt.xlabel('Average Sentiment Score')
    plt.ylabel('Daily Return')
    plt.tight_layout()
    plt.savefig(output_dir / 'sentiment_vs_return.png')
    plt.show()


def main():
    base = Path(__file__).resolve().parent.parent
    data_path = base / 'data' / 'real_financial_news.csv'
    output_dir = base / 'outputs'
    output_dir.mkdir(exist_ok=True)

    df = load_and_prepare_data(str(data_path))
    model, metrics = train_sentiment_model(df)

    print('Model Accuracy:', round(metrics['accuracy'], 4))
    print(metrics['report'])

    daily_sentiment = build_daily_sentiment(df)
    market_df = fetch_market_data('SPY', '2025-01-01', '2025-01-20')
    merged = merge_sentiment_with_market(daily_sentiment, market_df)

    output_csv = output_dir / 'sentiment_market_output.csv'
    merged.to_csv(output_csv, index=False)

    print('\nSaved output to:', output_csv)
    print('\nMerged Sentiment + Market Data:')
    print(merged.head())

    plot_sentiment_trend(daily_sentiment, output_dir)
    plot_market_trend(merged, output_dir)
    plot_sentiment_vs_return(merged, output_dir)


if __name__ == '__main__':
    main()