from minio import Minio
from datetime import timedelta
from utils.interfaces.s3 import S3
from config import logger


class MinioService(S3):
    def __init__(
            self,
            host_url: str,
            access_key: str,
            secret_key: str,
            options: dict = None
    ):
        super().__init__(host_url, access_key, secret_key, options)
        self.client = self.create_client()

    def create_client(self):
        try:
            self.client = Minio(
                self.host_url,
                access_key=self.access_key,
                secret_key=self.secret_key,
                secure=self.options.get('secure', False)
            )

            logger.info("Minio client created successfully")
            return self.client

        except Exception as e:
            raise ValueError(f"Error creating Minio client: {e}")

    def object_exists(self, bucket_name: str, object_name: str):
        objects = self.client.list_objects(bucket_name)
        for obj in objects:
            if obj.object_name == object_name:
                return True

    def list_buckets(self):
        try:
            buckets = self.client.list_buckets()
            logger.info("Buckets listed successfully")
            return [bucket.name for bucket in buckets]
        except Exception as e:
            logger.error(f"Error listing buckets: {e}")

    def bucket_exists(self, bucket_name: str):
        return self.client.bucket_exists(bucket_name)

    def create_bucket(self, bucket_name: str):
        self.client.make_bucket(bucket_name)

    def upload_file(self, bucket_name: str, file_path: str, object_name: str):
        self.client.fput_object(bucket_name, object_name, file_path)

    def download_file(self, bucket_name: str, object_name: str, file_path: str) -> None:
        self.client.fget_object(bucket_name, object_name, file_path)

    def list_objects(self, bucket_name: str) -> list:
        if self.client.bucket_exists(bucket_name):
            try:
                objects = self.client.list_objects(bucket_name)
                logger.info(f"Objects listed successfully in bucket {bucket_name}")
                return objects
            except Exception as e:
                logger.error(f"Error listing objects in bucket {bucket_name}: {e}")
        else:
            logger.error(f"Bucket {bucket_name} does not exist")
            return []

    def remove_object(self, bucket_name: str, object_name: str) -> None:
        self.client.remove_object(bucket_name, object_name)

    def remove_bucket(self, bucket_name: str) -> None:
        self.client.remove_bucket(bucket_name)

    def get_presigned_url(self, bucket_name: str, object_name: str, expires: dict) -> str:
        """
        :param bucket_name:
        :param object_name:
        :param expires: is a dictionary with the following keys
            - days
            - hours
            - minutes
            - seconds
        :return:
        """
        return self.client.presigned_get_object(bucket_name, object_name, expires=timedelta(**expires))
