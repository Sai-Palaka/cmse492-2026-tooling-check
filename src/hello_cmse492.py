"""Simple CSV reader for CMSE 492 tooling check."""

from pathlib import Path
import csv


def main() -> None:
    # Let's first just print a simple message.
    print("Hello from CMSE 492!")

    # Now let's load a small CSV file and compute a basic summary.
    # This tests that standard library modules can be imported and used.
    data_path = Path(__file__).resolve().parents[1] / "data" / "sample_data.csv"
    rows = []
    with data_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            rows.append({"name": row["name"], "value": int(row["value"])})

    total = sum(item["value"] for item in rows)
    average = total / len(rows) if rows else 0

    print(f"Loaded {len(rows)} rows from {data_path.name}")
    print(f"Total value: {total}")
    print(f"Average value: {average:.2f}")


if __name__ == "__main__":
    main()
