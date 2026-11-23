import csv
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]

TXT_FILE = (
    PROJECT_ROOT
    / "data"
    / "sample"
    / "txt"
    / "member_profiles_sample.txt"
)


def read_member_file():

    records = []

    with open(TXT_FILE, "r", encoding="utf-8") as file:

        reader = csv.reader(file, delimiter="|")

        for row in reader:

            # Remove empty boundary fields
            row = [value.strip() for value in row]

            if row and row[0] == "":
                row = row[1:]

            if row and row[-1] == "":
                row = row[:-1]

            if not row:
                continue

            records.append(row)

    # Identify header
    header = records[0]

    if header[0] != "H":
        raise ValueError("Header record must begin with H")

    column_names = header[1:]

    member_records = []

    for row in records[1:]:

        if row[0] != "D":
            print("Unexpected record type:", row[0])
            continue

        values = row[1:]

        if len(values) != len(column_names):
            print("Malformed record:", row)
            continue

        member_records.append(
            dict(zip(column_names, values))
        )

    print("Total member records:", len(member_records))

    print("First member:")
    print(member_records[0])

    return member_records


if __name__ == "__main__":
    read_member_file()