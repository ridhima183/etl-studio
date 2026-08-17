import pandas as pd
from etl.validate import validate

def test_valid_customer_data():
    df = pd.DataFrame([{
        "customer_id":1,"customer_name":"Test","email":"test@example.com",
        "city":"Hyderabad","state":"Telangana"
    }])
    assert validate(df) == []

def test_duplicate_customer_id():
    df = pd.DataFrame([
        {"customer_id":1,"customer_name":"A","email":"a@example.com","city":"Hyd","state":"TS"},
        {"customer_id":1,"customer_name":"B","email":"b@example.com","city":"Hyd","state":"TS"}
    ])
    assert any("duplicates" in x for x in validate(df))

def test_invalid_email():
    df = pd.DataFrame([{
        "customer_id":1,"customer_name":"Test","email":"bad-email",
        "city":"Hyderabad","state":"Telangana"
    }])
    assert any("Invalid email" in x for x in validate(df))
