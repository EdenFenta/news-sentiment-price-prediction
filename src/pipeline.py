from pathlib import Path
from src.data_loader import load_all_stocks
from src.indicators import add_indicators
from src.plotting import plot_stock

PROCESSED_DIR = Path("data/processed")
PROCESSED_DIR.mkdir(exist_ok=True)

# Load all stocks
stocks = load_all_stocks("data/raw")

# Add indicators, plot, and save
for ticker, df in stocks.items():
    df = add_indicators(df)
    plot_stock(df, ticker)
    stocks[ticker] = df  # update dictionary

    # Save processed CSV
    df.to_csv(PROCESSED_DIR / f"{ticker}_processed.csv", index=False)
    print(f"Saved processed data for {ticker}")
