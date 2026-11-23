
import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]

JSON_FILE = (
    PROJECT_ROOT
    / "data"
    / "sample"
    / "json"
    / "redemptions_sample.json"
)


def validate_redemptions():

    with open(JSON_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    errors = []
    valid_transactions = []
    invalid_transactions = []

    # Validate parent fields
    if not str(data.get("member_id", "")).strip():
        errors.append("Missing member_id")

    if not str(data.get("feed_date", "")).strip():
        errors.append("Missing feed_date")

    transactions = data.get("redemptions")

    if not isinstance(transactions, list):
        raise ValueError("redemptions must be a list")

    # Validate individual transactions
    for transaction in transactions:

        transaction_errors = []

        if not isinstance(transaction, dict):
            invalid_transactions.append({
                "transaction": transaction,
                "errors": ["Transaction must be an object"]
            })
            continue

        if not str(transaction.get("txn_id", "")).strip():
            transaction_errors.append("Missing txn_id")

        if not str(transaction.get("txn_date", "")).strip():
            transaction_errors.append("Missing txn_date")
        else:
            import pandas as pd

            parsed_date = pd.to_datetime(
                transaction["txn_date"],
                format="%Y%m%d",
                errors="coerce"
            )

            if pd.isna(parsed_date):
                transaction_errors.append("Invalid txn_date")

        miles = transaction.get("miles_redeemed")

        try:
            miles = float(miles)

            if miles < 0:
                transaction_errors.append(
                    "Miles cannot be negative"
                )

        except (TypeError, ValueError):
            transaction_errors.append(
                "Miles must be numeric"
            )

        if not str(transaction.get("partner", "")).strip():
            transaction_errors.append("Missing partner")

        if not str(transaction.get("status", "")).strip():
            transaction_errors.append("Missing status")

        if transaction_errors:
            invalid_transactions.append({
                "transaction": transaction,
                "errors": transaction_errors
            })
        else:
            valid_transactions.append(transaction)

    return valid_transactions, invalid_transactions, errors


if __name__ == "__main__":

    valid, invalid, errors = validate_redemptions()

    print("Valid transactions:", len(valid))
    print("Invalid transactions:", len(invalid))
    print("Feed-level errors:", errors)
