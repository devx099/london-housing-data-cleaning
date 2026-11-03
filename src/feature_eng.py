import pandas as pd

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Creating new features for ML."""
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['month_name'] = df['date'].dt.month_name().astype('category')

    # 2. Create a Binary Feature
    median_crimes = df['no_of_crimes'].median()
    df['is_high_crime'] = (df['no_of_crimes'] > median_crimes).astype(int).astype('category')

    # Rename columns
    df = df.rename(columns={
        'average_price': 'avg_price',
        'houses_sold': 'houses_sold_count',
        'borough_flag': 'is_borough'
    })

    return df