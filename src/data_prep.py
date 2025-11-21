import pandas as pd
from pathlib import Path

# File Paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"

RAW_NEWS_CSV = RAW_DATA_DIR / "raw_analyst_ratings.csv"
CLEAN_DATA_PATH = DATA_DIR / "clean_news.parquet"


# Functions
def load_news_csv(csv_path: Path) -> pd.DataFrame:
    """Read CSV and check required columns."""
    df = pd.read_csv(csv_path)

    expected_cols = ['headline', 'url', 'publisher', 'date', 'stock']
    missing_cols = [c for c in expected_cols if c not in df.columns]

    if missing_cols:
        raise ValueError(f"CSV is missing columns: {missing_cols}")

    return df[expected_cols].copy()


def process_headlines(df: pd.DataFrame) -> pd.DataFrame:
    """Clean headlines and create derived columns."""
    df['headline'] = df['headline'].astype(str).str.strip()

    # Character length
    df['headline_length_chars'] = df['headline'].str.len().fillna(0).astype(int)

    # Token count — simple + fast (no NLTK)
    df['headline_length_tokens'] = df['headline'].str.split().str.len()

    # Lowercase version
    df['headline_lower'] = df['headline'].str.lower()

    # Convert date to UTC datetime
    df['date'] = pd.to_datetime(df['date'], errors='coerce', utc=True)

    # Date only column
    df['date_only'] = df['date'].dt.date

    return df


def save_cleaned_news(df: pd.DataFrame, output_path: Path):
    """Save cleaned dataframe as parquet."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(output_path, index=False)
    print(f"Saved cleaned data to: {output_path}")


def run_data_pipeline():
    """Main pipeline."""
    if not RAW_NEWS_CSV.exists():
        print(f"File not found: {RAW_NEWS_CSV}")
        return

    print("Loading raw CSV...")
    df = load_news_csv(RAW_NEWS_CSV)

    print("Cleaning and processing headlines...")
    df = process_headlines(df)

    print("Saving clean parquet file...")
    save_cleaned_news(df, CLEAN_DATA_PATH)

    print("Data preparation complete!")


# Run Script
if __name__ == "__main__":
    run_data_pipeline()
