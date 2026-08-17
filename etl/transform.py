import pandas as pd

REQUIRED_COLUMNS = ["customer_id","customer_name","email","city","state"]

def transform(csv_df, api_df):
    combined = pd.concat([csv_df, api_df], ignore_index=True)
    missing = [c for c in REQUIRED_COLUMNS if c not in combined.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    combined = combined[REQUIRED_COLUMNS].copy()

    for col in ["customer_name","email","city","state"]:
        combined[col] = combined[col].astype("string").str.strip()

    combined["email"] = combined["email"].str.lower()
    combined["customer_id"] = pd.to_numeric(
        combined["customer_id"], errors="coerce"
    ).astype("Int64")

    # API is treated as the preferred/latest source for duplicate IDs.
    combined["_source_priority"] = 0
    api_ids = set(api_df["customer_id"].dropna().tolist()) if len(api_df) else set()
    combined.loc[combined["customer_id"].isin(api_ids), "_source_priority"] = 1

    return (combined.sort_values(["customer_id","_source_priority"])
            .drop_duplicates("customer_id", keep="last")
            .drop(columns="_source_priority")
            .reset_index(drop=True))
