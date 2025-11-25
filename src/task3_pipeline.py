import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from src.data_loader import load_all_stocks

# Load stock price data
stocks = load_all_stocks("data/raw")

# Load news
news = pd.read_parquet("data/clean_news.parquet")
news['date_only'] = pd.to_datetime(news['date_only'])

# Function to compute sentiment polarity
def compute_sentiment(text):
    return TextBlob(text).sentiment.polarity

# Loop through all tickers
for ticker, df in stocks.items():
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Merge news with stock prices by date
    merged = pd.merge(news, df, left_on='date_only', right_on='Date', how='inner')
    if merged.empty:
        print(f"No matching news for {ticker}")
        continue
    
    # Compute sentiment
    merged['sentiment'] = merged['headline'].apply(compute_sentiment)
    
    # Compute daily average sentiment
    daily_sentiment = merged.groupby('date_only')['sentiment'].mean().reset_index()
    
    # Compute daily stock returns
    df['daily_return'] = df['Close'].pct_change()
    
    # Merge daily sentiment with stock returns
    daily_data = pd.merge(daily_sentiment, df, left_on='date_only', right_on='Date', how='inner')
    
    # Compute correlation
    corr = daily_data['sentiment'].corr(daily_data['daily_return'])
    print(f"{ticker} - Pearson correlation: {corr:.4f}")
    
    # Plot sentiment vs daily returns
    plt.figure(figsize=(12,5))
    plt.scatter(daily_data['sentiment'], daily_data['daily_return'], alpha=0.5)
    plt.title(f"{ticker}: Daily Sentiment vs. Daily Return (corr={corr:.4f})")
    plt.xlabel("Average Daily Sentiment")
    plt.ylabel("Daily Return")
    plt.savefig(f"outputs/figs/{ticker}_sentiment_return.png")
    plt.close()
    
    # save merged dataset
    daily_data.to_csv(f"outputs/{ticker}_news_stock_merged.csv", index=False)