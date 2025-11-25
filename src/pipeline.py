# src/pipeline.py
from src.data_loader import load_all_stocks
from src.indicators import add_indicators
from src.plotting import plot_stock

# Load all stocks
stocks = load_all_stocks("data/raw")

# Add indicators & plot
for ticker, df in stocks.items():
    df = add_indicators(df)
    plot_stock(df, ticker)
    stocks[ticker] = df  # update with indicators
