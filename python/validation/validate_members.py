
import pandas as pd

from pathlib import Path


REQUIRED_COLUMNS = [
    "Member_Name",
    "Member_Id",
    "Enrollment_Date"
]

MAX_LENGTHS = {
    "Member_Name": 255,
    "Member_Id": 18,
    "Tier_Code": 5,
    "Agent_Name": 255,
    "State": 5,
    "Country": 5,
    "Post_Code": 5,
    "Is_Active": 1
}


def validate_members(df):

    df = df.copy()

    # Check that required columns exist
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # Initialize validation error column
    df["validation_errors"] = ""

    # 1. Mandatory field validation
    for column in REQUIRED_COLUMNS:

        missing = (
            df[column].isna()
            | df[column].astype(str).str.strip().eq("")
        )

        df.loc[missing, "validation_errors"] += (
            f"{column} is mandatory; "
        )

    # 2. Maximum length validation
    for column, max_length in MAX_LENGTHS.items():

        if column not in df.columns:
            continue

        values = df[column].fillna("").astype(str).str.strip()

        invalid = values.str.len() > max_length

        df.loc[invalid, "validation_errors"] += (
            f"{column} exceeds maximum length; "
        )

    # 3. Enrollment date validation: YYYYMMDD
    if "Enrollment_Date" in df.columns:

        values = df["Enrollment_Date"].fillna("").astype(str).str.strip()

        parsed = pd.to_datetime(
            values,
            format="%Y%m%d",
            errors="coerce"
        )

        invalid = values.ne("") & parsed.isna()

        df.loc[invalid, "validation_errors"] += (
            "Invalid Enrollment_Date; "
        )

    # 4. DOB validation: MMDDYYYY
    if "DOB" in df.columns:

        values = df["DOB"].fillna("").astype(str).str.strip()

        parsed = pd.to_datetime(
            values,
            format="%m%d%Y",
            errors="coerce"
        )

        invalid = values.ne("") & parsed.isna()

        df.loc[invalid, "validation_errors"] += (
            "Invalid DOB; "
        )

    # 5. Last flight date validation: YYYYMMDD
    if "Last_Flight_Date" in df.columns:

        values = (
            df["Last_Flight_Date"]
            .fillna("")
            .astype(str)
            .str.strip()
        )

        parsed = pd.to_datetime(
            values,
            format="%Y%m%d",
            errors="coerce"
        )

        invalid = values.ne("") & parsed.isna()

        df.loc[invalid, "validation_errors"] += (
            "Invalid Last_Flight_Date; "
        )

    # 6. Separate valid and invalid records
    df["is_valid"] = df["validation_errors"].eq("")

    valid_records = df[df["is_valid"]].copy()

    invalid_records = df[~df["is_valid"]].copy()

    return valid_records, invalid_records

def find_duplicate_members(df):

    duplicate_mask = df.duplicated(
        subset=["Member_Id"],
        keep=False
    )

    duplicates = df[duplicate_mask].copy()

    unique_records = df[~duplicate_mask].copy()

    return unique_records, duplicates

def save_quarantine(invalid_records):

    project_root = Path(__file__).resolve().parents[2]

    quarantine_dir = project_root / "data" / "quarantine"

    quarantine_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = quarantine_dir / "invalid_members.csv"

    invalid_records.to_csv(
        output_file,
        index=False
    )

    print("Invalid records saved to:", output_file)

def generate_quality_report(total, valid, invalid):

    report = {
        "total_records": total,
        "valid_records": len(valid),
        "invalid_records": len(invalid)
    }

    print("\nDATA QUALITY REPORT")
    print("-------------------")

    for metric, count in report.items():
        print(f"{metric}: {count}")

    return report