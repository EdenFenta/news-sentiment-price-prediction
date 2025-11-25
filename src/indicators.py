import talib

def add_indicators(df):
    df["SMA_10"] = talib.SMA(df["Close"], timeperiod=10)
    df["SMA_50"] = talib.SMA(df["Close"], timeperiod=50)
    df["RSI_14"] = talib.RSI(df["Close"], timeperiod=14)
    df["MACD"], df["MACD_signal"], df["MACD_hist"] = talib.MACD(df["Close"])
    return df
