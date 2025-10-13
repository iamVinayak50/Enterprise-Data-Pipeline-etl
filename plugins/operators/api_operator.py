import requests
import pandas as pd

def fetch_api_data(url):
    res = requests.get(url)
    res.raise_for_status()
    return pd.DataFrame(res.json().get("entries", []))
