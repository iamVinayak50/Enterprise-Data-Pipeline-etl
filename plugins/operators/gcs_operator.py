from google.cloud import storage
import pandas as pd
import json

def read_gcs_json(bucket_name, file_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    content = blob.download_as_text()
    data = json.loads(content)
    return pd.DataFrame(data)
