from google.cloud import bigquery

def query_bq_to_df(query):
    client = bigquery.Client()
    return client.query(query).to_dataframe()

def load_to_bq(df, table_id):
    client = bigquery.Client()
    job = client.load_table_from_dataframe(df, table_id)
    job.result()
