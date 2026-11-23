
import pandas as pd

from python.validation.validate_members import (
    validate_members,
    save_quarantine
)


# Step 1: Create sample input records
sample_data = pd.DataFrame([
    {
        "Member_Name": "Elena",
        "Member_Id": "223457",
        "Enrollment_Date": "20101012",
        "DOB": "03051985"
    },
    {
        "Member_Name": "",
        "Member_Id": "223458",
        "Enrollment_Date": "20101012",
        "DOB": "03051985"
    },
    {
        "Member_Name": "Nora",
        "Member_Id": "",
        "Enrollment_Date": "20201312",
        "DOB": "03051985"
    },
    {
        "Member_Name": "Jacob",
        "Member_Id": "2256",
        "Enrollment_Date": "20101012",
        "DOB": ""
    }
])


# Step 2: Validate the records
valid_records, invalid_records = validate_members(
    sample_data
)


# Step 3: Display valid records
print("\nVALID RECORDS:")
print(valid_records)


# Step 4: Display invalid records
print("\nINVALID RECORDS:")
print(invalid_records)


# Step 5: Save invalid records in quarantine
save_quarantine(invalid_records)
