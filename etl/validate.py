import re

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def validate(df):
    errors = []
    if df.empty:
        errors.append("Dataset is empty")
    if df["customer_id"].isna().any():
        errors.append("customer_id contains NULL values")
    if not df["customer_id"].is_unique:
        errors.append("customer_id contains duplicates")

    for col in ["customer_name","city","state"]:
        if df[col].isna().any() or (df[col].str.len() == 0).any():
            errors.append(f"{col} contains NULL/empty values")

    invalid = ~df["email"].fillna("").str.match(EMAIL_RE)
    if invalid.any():
        errors.append(f"Invalid email count: {int(invalid.sum())}")
    return errors
