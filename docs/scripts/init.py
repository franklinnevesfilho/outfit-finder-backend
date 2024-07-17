import os
from minio import Minio


# Minio connection
minio_buckets = ['images', 'models']

minio_client = Minio(
    'minio:9000',
    access_key='minioadmin',
    secret_key='minioadminpassword',
    secure=False
)

for bucket in minio_buckets:
    if not minio_client.bucket_exists(bucket):
        minio_client.make_bucket(bucket)
        print(f"Bucket {bucket} created successfully")
    else:
        print(f"Bucket {bucket} already exists")

folder = 'scripts/models'

# upload models to minio
model_files = os.listdir(folder)

for model_file in model_files:
    minio_client.fput_object('models', model_file, f'{folder}/{model_file}')
    print(f"Model {model_file} uploaded successfully")
