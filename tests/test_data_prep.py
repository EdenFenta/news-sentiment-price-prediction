from src.data_prep import process_headlines
import pandas as pd

def test_headline_length_columns():
    sample = pd.DataFrame({
        "headline": ["Hello World", "Python is great!"],
        "url": ["url1", "url2"],
        "publisher": ["pub1", "pub2"],
        "date": ["2025-11-21", "2025-11-21"],
        "stock": ["AAPL", "GOOG"]
    })

    df = process_headlines(sample)

    # Check that new columns exist
    assert "headline_length_chars" in df.columns
    assert "headline_length_tokens" in df.columns
    assert "headline_lower" in df.columns
    assert "date_only" in df.columns

    # Check lengths are computed correctly
    assert df["headline_length_chars"].iloc[0] == len("Hello World")
    assert df["headline_length_tokens"].iloc[1] == 3