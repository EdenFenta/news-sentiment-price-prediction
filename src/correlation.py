
import pandas as pd
from textblob import TextBlob
from src.data_loader import load_all_stocks

# Load news data
news = pd.read_parquet("data/clean_news.parquet")
news['date_only'] = pd.to_datetime(news['date_only'])

# Load stock price data
stocks = load_all_stocks("data/raw")

# Function to calculate sentiment score
def sentiment_score(text):
    return TextBlob(text).sentiment.polarity  # ranges from -1 to 1

# Add sentiment scores to news
news['sentiment'] = news['headline'].apply(sentiment_score)

# Store correlations for each stock
correlations = {}

for ticker, df in stocks.items():
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Merge news and stock prices on date
    merged = pd.merge(news, df, left_on='date_only', right_on='Date', how='inner')
    
    if merged.empty:
        print(f"No overlapping dates for {ticker}")
        continue
    
    # Calculate daily stock returns
    merged['daily_return'] = merged['Close'].pct_change()
    
    # Aggregate daily sentiment (mean if multiple headlines per day)
    daily_sentiment = merged.groupby('date_only')['sentiment'].mean().reset_index()
    daily_data = pd.merge(daily_sentiment, df, left_on='date_only', right_on='Date', how='inner')
    
    # Calculate correlation
    corr = daily_data['sentiment'].corr(daily_data['Close'].pct_change())
    correlations[ticker] = corr
    print(f"{ticker} sentiment-stock correlation: {corr:.4f}")
    
# convert to DataFrame for reporting
corr_df = pd.DataFrame(list(correlations.items()), columns=['Ticker', 'Sentiment_Correlation'])
corr_df.to_csv("outputs/sentiment_stock_correlation.csv", index=False)
print("\nAll correlations saved to outputs/sentiment_stock_correlation.csv")
