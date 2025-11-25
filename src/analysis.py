import pandas as pd
from scipy.stats import pearsonr


def calculate_daily_returns(stock_df):
    """
    Computes daily stock returns
    """
    stock_df = stock_df.sort_values('Date')
    stock_df['daily_return'] = stock_df['Close'].pct_change()
    return stock_df


def merge_news_and_stocks(news_df, stock_df):
    """
    Merges news and stock data by date
    """
    news_df['date_only'] = pd.to_datetime(news_df['date']).dt.date
    stock_df['Date'] = pd.to_datetime(stock_df['Date']).dt.date

    merged = pd.merge(news_df, stock_df, left_on='date_only', right_on='Date', how='inner')
    return merged


def calculate_correlation(merged_df):
    """
    Calculates Pearson correlation between sentiment and stock returns
    """
    merged_df = merged_df.dropna(subset=['sentiment_score', 'daily_return'])

    corr, p_value = pearsonr(merged_df['sentiment_score'], merged_df['daily_return'])

    return corr, p_value
