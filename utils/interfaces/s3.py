from abc import ABC, abstractmethod


class S3(ABC):
    def __init__(
            self,
            host_url: str,
            access_key: str,
            secret_key: str,
            options: dict = None
    ):
        self.access_key = access_key
        self.secret_key = secret_key
        self.host_url = host_url
        self.options = options

    @abstractmethod
    def object_exists(self, bucket_name: str, object_name: str):
        pass

    @abstractmethod
    def list_buckets(self):
        pass

    @abstractmethod
    def bucket_exists(self, bucket_name: str):
        pass

    @abstractmethod
    def create_bucket(self, bucket_name: str):
        pass

    @abstractmethod
    def upload_file(self, bucket_name: str, file_path: str, object_name: str):
        pass

    @abstractmethod
    def download_file(self, bucket_name: str, object_name: str, file_path: str):
        pass

    @abstractmethod
    def list_objects(self, bucket_name: str):
        pass

    @abstractmethod
    def remove_object(self, bucket_name: str, object_name: str):
        pass

    @abstractmethod
    def remove_bucket(self, bucket_name: str):
        pass

    @abstractmethod
    def create_client(self):
        pass

    @abstractmethod
    def get_presigned_url(self, bucket_name: str, object_name: str, expires: int):
        pass


