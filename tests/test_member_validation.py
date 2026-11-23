import pandas as pd

from python.validation.validate_members import validate_members


def test_valid_member():

    df = pd.DataFrame([
        {
            "Member_Name": "Elena",
            "Member_Id": "223457",
            "Enrollment_Date": "20101012",
            "DOB": "03051985"
        }
    ])

    valid, invalid = validate_members(df)

    assert len(valid) == 1
    assert len(invalid) == 0


def test_missing_member_id():

    df = pd.DataFrame([
        {
            "Member_Name": "Elena",
            "Member_Id": "",
            "Enrollment_Date": "20101012"
        }
    ])

    valid, invalid = validate_members(df)

    assert len(valid) == 0
    assert len(invalid) == 1

    assert "Member_Id is mandatory" in (
        invalid.iloc[0]["validation_errors"]
    )


def test_invalid_enrollment_date():

    df = pd.DataFrame([
        {
            "Member_Name": "Nora",
            "Member_Id": "223459",
            "Enrollment_Date": "20201312"
        }
    ])

    valid, invalid = validate_members(df)

    assert len(valid) == 0
    assert len(invalid) == 1

    assert "Invalid Enrollment_Date" in (
        invalid.iloc[0]["validation_errors"]
    )