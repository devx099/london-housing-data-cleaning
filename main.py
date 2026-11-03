import pandas as pd

from src.load_data import load_raw_data
from src.clean_data import clean_housing_data
from src.feature_eng import engineer_features
from src.save_data import save_processed_data


def main():
    print("Starting London Housing Data Pipeline...")

    # Step 1: Loading raw data
    print("1. Loading raw data...")
    raw_df = load_raw_data('data/raw/housing_in_london_monthly_variables.csv')

    # Step 2: Clean
    print("2. Cleaning data...")
    clean_df = clean_housing_data(raw_df)

    # Step 3: Feature Engineering
    print("3. Engineering features...")
    final_df = engineer_features(clean_df)

    # Step 4: Save
    print("4. Saving processed data...")
    save_processed_data(final_df, 'data/processed/cleaned.parquet')

    print("✅ Pipeline completed successfully!")


if __name__ == "__main__":
    main()