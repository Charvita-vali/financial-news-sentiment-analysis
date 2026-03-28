"""
Market analysis module.
Maps sentiment to numerical scores and compares with market data.
"""
import pandas as pd
import yfinance as yf

SENTIMENT_MAP = {
    'Positive': 1,
    'Neutral': 0,
    'Negative': -1
}

def build_daily_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out['date'] = pd.to_datetime(out['date'])
    out['sentiment_score'] = out['sentiment_label'].map(SENTIMENT_MAP)
    daily = out.groupby('date', as_index=False)['sentiment_score'].mean()
    daily.rename(columns={'sentiment_score': 'avg_sentiment_score'}, inplace=True)
    return daily

def fetch_market_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    prices = yf.download(ticker, start=start, end=end, progress=False, auto_adjust=True)
    if prices.empty:
        return pd.DataFrame(columns=['date', 'close', 'daily_return'])
    prices = prices.reset_index()[['Date', 'Close']]
    prices.columns = ['date', 'close']
    prices['daily_return'] = prices['close'].pct_change()
    prices['date'] = pd.to_datetime(prices['date'])
    return prices

def merge_sentiment_with_market(daily_sentiment: pd.DataFrame, market_df: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(daily_sentiment, market_df, on='date', how='left')
    return merged
