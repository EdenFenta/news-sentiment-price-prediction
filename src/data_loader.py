import pandas as pd
import glob
import os

def load_all_stocks(data_path="data/raw"):
    stock_files = glob.glob(os.path.join(data_path, "*.csv"))
    stock_data = {}
    
    for file in stock_files:
        ticker = os.path.basename(file).replace(".csv", "")
        df = pd.read_csv(file, parse_dates=["Date"])
        df.sort_values("Date", inplace=True)
        df.reset_index(drop=True, inplace=True)
        stock_data[ticker] = df
    
    return stock_data
