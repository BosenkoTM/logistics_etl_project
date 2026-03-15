import pandas as pd
from logistics_etl import clean_logistics_data

def test_clean_logistics_data():
    raw_data = [
        {"tracking_number": "TRK123", "status": "In Transit"},
        {"tracking_number": None, "status": "Lost"}
    ]
    df = clean_logistics_data(raw_data)
    assert len(df) == 1
    assert df.iloc[0]['tracking_number'] == "TRK123"