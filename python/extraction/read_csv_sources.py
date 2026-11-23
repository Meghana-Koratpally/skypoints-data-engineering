
from pathlib import Path
import pandas as pd


# Find project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# CSV input directory
CSV_DIR = PROJECT_ROOT / "data" / "sample" / "csv"


def read_csv_file(file_path):
    """
    Read a CSV file and return a pandas DataFrame.
    """

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    dataframe = pd.read_csv(file_path)

    return dataframe


def inspect_csv(file_name):

    file_path = CSV_DIR / file_name

    dataframe = read_csv_file(file_path)

    print("\n--------------------------------")
    print("FILE:", file_name)
    print("--------------------------------")

    print("Number of rows and columns:")
    print(dataframe.shape)

    print("\nColumn names:")
    print(list(dataframe.columns))

    print("\nFirst five records:")
    print(dataframe.head())

    print("\nData types:")
    print(dataframe.dtypes)

    print("\nMissing values:")
    print(dataframe.isnull().sum())

    return dataframe


def main():

    csv_files = [
        "USA.csv",
        "IND.csv",
        "AUS.csv"
    ]

    extracted_data = {}

    for file_name in csv_files:

        dataframe = inspect_csv(file_name)

        country = file_name.split(".")[0]

        extracted_data[country] = dataframe

    print("\n========== EXTRACTION SUMMARY ==========")

    for country, dataframe in extracted_data.items():

        print(
            country,
            "records:",
            len(dataframe)
        )


if __name__ == "__main__":
    main()
