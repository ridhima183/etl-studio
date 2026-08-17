import pandas as pd
from etl.transform import transform

def test_api_wins_for_duplicate_customer():
    csv_df = pd.DataFrame([{
        "customer_id":1,"customer_name":"Old","email":"old@example.com",
        "city":"Hyderabad","state":"Telangana"
    }])
    api_df = pd.DataFrame([{
        "customer_id":1,"customer_name":"Latest","email":"latest@example.com",
        "city":"Bengaluru","state":"Karnataka"
    }])
    result = transform(csv_df, api_df)
    assert len(result) == 1
    assert result.iloc[0]["customer_name"] == "Latest"
