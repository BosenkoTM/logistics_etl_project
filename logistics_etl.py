import pandas as pd

def clean_logistics_data(data: list) -> pd.DataFrame:
    # Имитация очистки данных логистики (удаление пустых трек-номеров)
    df = pd.DataFrame(data)
    if 'tracking_number' in df.columns:
        df = df.dropna(subset=['tracking_number'])
    return df

if __name__ == "__main__":
    raw_data = [
        {"tracking_number": "TRK123", "status": "In Transit"},
        {"tracking_number": None, "status": "Lost"},
        {"tracking_number": "TRK124", "status": "Delivered"}
    ]
    cleaned_data = clean_logistics_data(raw_data)
    print("ETL Processed data:")
    print(cleaned_data)