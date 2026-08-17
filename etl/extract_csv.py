from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = ["customer_id","customer_name","email","city","state"]

def extract_csv(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")
    df = pd.read_csv(path)
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing CSV columns: {missing}")
    return df[REQUIRED_COLUMNS]
