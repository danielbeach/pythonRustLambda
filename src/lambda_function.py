from deltalake import write_deltalake
import os
from datetime import datetime
from pyarrow import fs
import pyarrow.dataset as ds


AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")

def handler(event, context):
    t1 = datetime.now()
    s3 = fs.S3FileSystem(access_key=AWS_ACCESS_KEY_ID, secret_key=AWS_SECRET_ACCESS_KEY)
    dataset = ds.dataset(filesystem=s3, source="confessions-of-a-data-guy/daft-large-data/",format='csv')


    write_deltalake(
            's3://confessions-of-a-data-guy/python-rurst/delta-table',
            dataset,
            mode="overwrite",
            engine="rust",
        )
    t2 = datetime.now()
    print(f"Time taken: {t2-t1}")