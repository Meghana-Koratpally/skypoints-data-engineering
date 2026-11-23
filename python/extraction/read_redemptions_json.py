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


def read_redemption_file():

    with open(JSON_FILE, "r", encoding="utf-8") as file:

        data = json.load(file)

    print("Member ID:", data["member_id"])

    print("Feed date:", data["feed_date"])

    print(
        "Number of redemptions:",
        len(data["redemptions"])
    )

    print("\nIndividual transactions:")

    for transaction in data["redemptions"]:

        print(transaction)

    return data


if __name__ == "__main__":
    read_redemption_file()