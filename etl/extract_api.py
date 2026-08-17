import pandas as pd
import requests

def extract_api(url, timeout=10):
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    payload = response.json()
    if not isinstance(payload, list):
        raise ValueError("API response must be a JSON list")
    return pd.DataFrame(payload)
