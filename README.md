# FNS_PID Week 1 - Task 1

## Description
The goal is to clean, process, and analyze news headlines to extract insights on trends and publisher activity.

## Folder Structure
- `.vscode/`               # VSCode settings
- `.github/workflows/`     # CI workflow (unittests.yml)
- `.gitignore`
- `requirements.txt`       # Python dependencies
- `README.md`
- `src/`                   # Source code
  - `__init__.py`
  - `data_prep.py`         # Data cleaning scripts
  - `eda.py`               # EDA helper functions
  - `indicators.py`        # (Task 2 later)
  - `sentiment.py`         # (Task 3 later)
- `notebooks/`             # Jupyter notebooks
  - `01_eda.ipynb`
- `tests/`                 # Unit tests
  - `test_data_prep.py`
- `scripts/`               # Optional scripts
- `outputs/figs/`          # Figures generated from EDA

## Getting Started
1. Clone repository:
   ```
   git clone <your_repo_url>
   ```

2. Create and activate virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate   # Mac/Linux
   .venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running Data Preparation
4. Run data preparation script:
   ```
   python src/data_prep.py
   ```
   - Loads raw CSV from `data/raw/raw_analyst_ratings.csv`
   - Cleans headlines and computes derived columns:
     - `headline_length_chars`
     - `headline_length_tokens`
     - `headline_lower`
     - `date_only`
   - Saves cleaned data to `data/clean_news.parquet`

## Running EDA
5. Open notebook for EDA:
   ```
   jupyter notebook notebooks/01_eda.ipynb
   ```
   - Analyze headline lengths, publisher counts, daily trends
   - Keyword extraction and optional topic modeling
   - Save figures to `outputs/figs/`

## Running Tests
6. Run tests:
   ```
   export PYTHONPATH=.   # if imports fail
   pytest tests/
   ```

## Git Workflow
7. Git workflow:
   ```
   git checkout -b task-1
   git add .
   git commit -m 'Task-1: data prep and EDA'
   git push -u origin task-1
   # Later create PR: task-1 -> main
   ```