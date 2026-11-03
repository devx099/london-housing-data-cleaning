import pandas as pd
import os


def load_raw_data(file_path: str) -> pd.DataFrame:
    """
    Loads raw CSV data from the specified file path.

    Args: file_path (str): Path to the raw CSV file.

    Returns: pd.DataFrame: The loaded data as a Pandas DataFrame.

    Raises: FileNotFoundError: If the file does not exist at the given path.
    """

    # Check if file exists or not and raise error if not
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: Could not find file at '{file_path}'")

    # Load the CSV if path exists
    df = pd.read_csv(file_path)

    print(f"Data loaded successfully from {file_path}")

    return df