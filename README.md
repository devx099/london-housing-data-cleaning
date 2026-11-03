# 🏠 London Housing Data Cleaning & Feature Engineering Pipeline

## 🎯 Objective
This project takes raw, messy monthly housing data for London boroughs and transforms it into a clean, Machine Learning-ready dataset. The goal is to handle missing values, optimize memory usage, and engineer temporal and binary features suitable for predictive modeling (e.g., forecasting average house prices).

## 📊 Dataset Source
- **Original Source:** [Housing in London by Justinas Cirtautas (Kaggle)](https://www.kaggle.com/datasets/justinas/housing-in-london)
- **File Used:** `housing_in_london_monthly_variables.csv`

## 🧹 Key Data Cleaning Steps
1. **Type Conversion:** Converted `date` to `datetime64[ns]` to enable time-series operations.
2. **Text Standardization:** Applied `.str.title()` to the `area` column to fix inconsistent casing (e.g., "city of london" → "City of London").
3. **Memory Optimization:** Downcasted low-cardinality string columns (`area`, `code`) and binary flags (`borough_flag`) to the `category` dtype, reducing memory usage by ~37%.
4. **Missing Value Imputation:** 
   - `houses_sold`: Filled 94 missing values (~0.7%) with the column **median** to preserve distribution.
   - `no_of_crimes`: Filled 6,110 missing values (~45%) with `0`, with the assumption that missing historical records indicate zero reported crimes for that month.

## ⚙️ Feature Engineering for ML
To make the dataset ready for tree-based models (Random Forest, XGBoost) or regression, the following features were engineered:
- `year` & `month`: Extracted from the `date` column to capture seasonality and long-term trends.
- `month_name`: Categorical representation of the month for one-hot encoding.
- `is_high_crime`: A binary feature (`1` or `0`) indicating if the monthly crime count exceeds the dataset's median, helping models capture non-linear thresholds.
- **Column Renaming:** Standardized all columns to `snake_case` (e.g., `average_price` → `avg_price`) for cleaner Scikit-Learn pipeline integration.

## 🚀 How to Use
1. Clone this repository.
2. Install dependencies: `pip install pandas numpy pyarrow`
3. Load the optimized dataset in Python:
   ```python
   import pandas as pd
   df = pd.read_parquet('cleaned_london_housing.parquet')
