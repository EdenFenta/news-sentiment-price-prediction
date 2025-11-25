import pandas as pd
import matplotlib.pyplot as plt

def stock_data_overview(stocks_df):
    print("\nStock Data Info:")
    print(stocks_df.info())
    print("\nMissing Values:")
    print(stocks_df.isnull().sum())


def news_data_overview(news_df):
    print("\nNews Data Info:")
    print(news_df.info())
    print("\nMissing Values:")
    print(news_df.isnull().sum())


def plot_stock_price(stocks_df, ticker):
    df = stocks_df.copy()
    df['Date'] = pd.to_datetime(df['Date'])

    stock = df[df['Ticker'] == ticker]

    plt.figure()
    plt.plot(stock['Date'], stock['Close'])
    plt.title(f"{ticker} Closing Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()
