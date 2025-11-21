#!/bin/bash

# Project: FNS_PID Week 1 - Task 1

## Description:
### Repository for Task 1: Data ingestion and EDA on financial news.
 echo "The goal is to clean, process, and analyze news headlines to extract insights on trends and publisher activity."

# Folder Structure:
 echo ".vscode/               # VSCode settings"
 echo ".github/workflows/     # CI workflow (unittests.yml)"
 echo ".gitignore"
 echo "requirements.txt       # Python dependencies"
 echo "README.md"
 echo "src/                   # Source code"
   echo "__init__.py"
   echo "data_prep.py         # Data cleaning scripts"
   echo "eda.py               # EDA helper functions"
   echo "indicators.py        # (Task 2 later)"
   echo "sentiment.py         # (Task 3 later)"
 echo "notebooks/             # Jupyter notebooks"
   echo "01_eda.ipynb"
 echo "tests/                 # Unit tests"
   echo "test_data_prep.py"
 echo "scripts/               # Optional scripts"
 echo "outputs/figs/          # Figures generated from EDA"

# Getting Started:

echo "1. Clone repository:"
echo "   git clone <your_repo_url>"

echo "2. Create and activate virtual environment:"
echo "   python -m venv .venv"
echo "   source .venv/bin/activate   # Mac/Linux"
echo "   .venv\\Scripts\\activate    # Windows"

echo "3. Install dependencies:"
echo "   pip install -r requirements.txt"

# Running Data Preparation:

echo "4. Run data preparation script:"
echo "   python src/data_prep.py"
echo "   - Loads raw CSV from data/raw/raw_analyst_ratings.csv"
echo "   - Cleans headlines and computes derived columns:"
echo "       - headline_length_chars"
echo "       - headline_length_tokens"
echo "       - headline_lower"
echo "       - date_only"
echo "   - Saves cleaned data to data/clean_news.parquet"

# Running EDA:

echo "5. Open notebook for EDA:"
echo "   jupyter notebook notebooks/01_eda.ipynb"
echo "   - Analyze headline lengths, publisher counts, daily trends"
echo "   - Keyword extraction and optional topic modeling"
echo "   - Save figures to outputs/figs/"

# Running Tests:

echo "6. Run tests:"
echo "   export PYTHONPATH=.   # if imports fail"
echo "   pytest tests/"

# Git Workflow:

echo "7. Git workflow:"
echo "   git checkout -b task-1"
echo "   git add ."
echo "   git commit -m 'Task-1: data prep and EDA'"
echo "   git push -u origin task-1"
echo "   # Later create PR: task-1 -> main"

# ==============================================
