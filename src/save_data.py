import pandas as pd
import os

def save_processed_data(df: pd.DataFrame, output_path: str, format: str = 'parquet') -> None:
    """
    Saves the processed DataFrame to disk.

    Args:
        df (pd.DataFrame): The cleaned/processed DataFrame to save.
        output_path (str): The file path where the data should be saved.
        format (str, optional): The file format. Either 'parquet' or 'csv'.
                                Defaults to 'parquet'.

    Raises:
        ValueError: If an unsupported format is specified.
        OSError: If the directory cannot be created or file cannot be written.
    """
    # Ensure the output directory exists
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    # Save based on format
    if format.lower() == 'parquet':
        df.to_parquet(output_path, index=False, engine='pyarrow')
        print(f"Saved Parquet file to: {output_path}")
        print(f"File size: {os.path.getsize(output_path) / 1024:.2f} KB")

    elif format.lower() == 'csv':
        df.to_csv(output_path, index=False)
        print(f"Saved CSV file to: {output_path}")
        print(f"File size: {os.path.getsize(output_path) / 1024:.2f} KB")

    else:
        raise ValueError(f"Unsupported format: '{format}'. Use 'parquet' or 'csv'.")