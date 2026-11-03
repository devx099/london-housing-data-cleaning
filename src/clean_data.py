import pandas as pd


def clean_housing_data(df: pd.DataFrame) -> pd.DataFrame:
    """Takes raw dataframe and returns a cleaned dataframe."""
    # Convert 'date' to actual datetime objects
    df['date'] = pd.to_datetime(df['date'])


    # Standardize text
    df['area'] = (df['area'].str.title())


    # Optimizing Memory
    df['area'] = df['area'].astype('category')
    df['code'] = df['code'].astype('category')
    df['borough_flag'] = df['borough_flag'].astype('category')


    # Handle missing values

    # For houses_sold (only 94 missing), fill with the median of the column
    median_houses_sold = df['houses_sold'].median()
    df['houses_sold'] = df['houses_sold'].fillna(median_houses_sold)

    # For no_of_crimes (6110 missing), fill with 0.
    # Assuming since there is no data about no_of_crimes, they must be 0
    df['no_of_crimes'] = df['no_of_crimes'].fillna(0)

    return df