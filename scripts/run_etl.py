from pathlib import Path
from etl.extract_csv import extract_csv
from etl.extract_api import extract_api
from etl.transform import transform
from etl.validate import validate
from etl.load import load_to_mysql

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "customers.csv"
API_URL = "http://127.0.0.1:5000/customers"

def main():
    print("=" * 60)
    print("CSV + API -> Pandas -> MySQL ETL")
    print("=" * 60)

    csv_df = extract_csv(CSV_PATH)
    print(f"CSV records: {len(csv_df)}")

    api_df = extract_api(API_URL)
    print(f"API records: {len(api_df)}")

    final_df = transform(csv_df, api_df)
    print(f"Final records after deduplication: {len(final_df)}")

    errors = validate(final_df)
    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f" - {error}")
        raise SystemExit(1)

    print("VALIDATION PASSED")
    load_to_mysql(final_df)
    print("LOAD COMPLETED")

if __name__ == "__main__":
    main()
