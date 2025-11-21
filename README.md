# ========================================================
# Project: FNS_PID Week 1 - Task 1
# ========================================================
# Description:
# This repository contains code for Task 1: Data ingestion
# and exploratory data analysis (EDA) on financial news
# datasets. The goal is to clean, process, and analyze
# news headlines to extract insights on trends and publisher activity.
#
# --------------------------------------------------------
# Folder Structure:
# --------------------------------------------------------
# ├── .vscode/                 # VSCode workspace settings
# ├── .github/
# │   └── workflows/
# │       └── unittests.yml    # GitHub Actions CI workflow
# ├── .gitignore
# ├── requirements.txt         # Python dependencies
# ├── README.md
# ├── src/                     # Source code
# │   ├── __init__.py
# │   ├── data_prep.py         # Data cleaning scripts
# │   ├── eda.py               # EDA helper functions
# │   ├── indicators.py        # (Task 2 later)
# │   └── sentiment.py         # (Task 3 later)
# ├── notebooks/
# │   └── 01_eda.ipynb         # EDA notebook
# ├── tests/
# │   └── test_data_prep.py    # Unit tests for data prep
# ├── scripts/                 # Optional scripts folder
# └── outputs/
#     └── figs/                # Figures generated from EDA
#
# --------------------------------------------------------
# Getting Started:
# --------------------------------------------------------
# 1. Clone the repository
#    git clone <your_repo_url>
# 2. Create and activate virtual environment
#    python -m venv .venv
#    source .venv/bin/activate       # Mac/Linux
#    .venv\Scripts\activate          # Windows
# 3. Install dependencies
#    pip install -r requirements.txt
#
# --------------------------------------------------------
# Running Data Preparation:
# --------------------------------------------------------
# python src/data_prep.py
# This will:
# - Load raw CSV from data/raw/raw_analyst_ratings.csv
# - Clean headlines, compute derived columns:
#     - headline_length_chars
#     - headline_length_tokens
#     - headline_lower
#     - date_only
# - Save cleaned data to data/clean_news.parquet
#
# --------------------------------------------------------
# Running EDA:
# --------------------------------------------------------
# Open Jupyter notebook
# jupyter notebook notebooks/01_eda.ipynb
# Perform analysis:
# - Headline length stats
# - Publisher article counts
# - Daily trends and spikes
# - Keyword extraction
# - Optional: LDA topic modeling
# Save figures to outputs/figs/
#
# --------------------------------------------------------
# Running Tests:
# --------------------------------------------------------
# pytest tests/
# Ensure PYTHONPATH is set if imports fail:
# export PYTHONPATH=.
#
# --------------------------------------------------------
# Git Workflow:
# --------------------------------------------------------
# 1. Create branch for task-1
#    git checkout -b task-1
# 2. Commit frequently with descriptive messages
#    git add .
#    git commit -m "Task-1: data prep and EDA"
# 3. Push branch
#    git push -u origin task-1
# 4. Later, create PR: task-1 → main
# ========================================================