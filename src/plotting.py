# src/plotting.py
import matplotlib.pyplot as plt
import os

def plot_stock(df, ticker):
    os.makedirs("outputs/figs", exist_ok=True)  # ensure folder exists
    plt.figure(figsize=(12,6))
    plt.plot(df["Date"], df["Close"], label="Close")
    plt.plot(df["Date"], df["SMA_10"], label="SMA_10")
    plt.plot(df["Date"], df["SMA_50"], label="SMA_50")
    plt.title(f"{ticker} Price & Moving Averages")
    plt.legend()
    plt.savefig(f"outputs/figs/{ticker}_indicators.png")
    plt.close()
