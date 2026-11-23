
from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]

CSV_DIR = PROJECT_ROOT / "data" / "sample" / "csv"


def profile_csv(file_name):

    file_path = CSV_DIR / file_name

    if not file_path.exists():
        raise FileNotFoundError(file_path)

    # Read source data as strings to avoid
    # automatically changing source values.
    df = pd.read_csv(file_path, dtype=str)

    print("\n================================")
    print("DATA PROFILE:", file_name)
    print("================================")

    # Total rows and columns
    print("\nShape:")
    print(df.shape)

    # Column names
    print("\nColumns:")
    print(list(df.columns))

    # Data types
    print("\nData types:")
    print(df.dtypes)

    # Missing values
    print("\nMissing values:")
    print(df.isna().sum())

    # Blank values
    print("\nBlank values:")
    print(
        df.apply(
            lambda column: column.str.strip().eq("").sum()
        )
    )

    # Duplicate rows
    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    # Distinct values
    print("\nDistinct values:")
    print(df.nunique(dropna=True))

    return df


if __name__ == "__main__":

    files = [
        "USA.csv",
        "IND.csv",
        "AUS.csv"
    ]

    for file_name in files:

        profile_csv(file_name)
