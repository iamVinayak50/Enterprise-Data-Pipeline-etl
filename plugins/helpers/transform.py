def transform_api_data(df):
    df["processed_at"] = pd.Timestamp.now()
    return df
