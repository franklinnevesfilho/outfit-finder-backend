from utils.interfaces.s3 import S3
from config import logger


class S3Factory:
    @staticmethod
    def get_s3(s3_type: str, host_url: str, access_key: str, secret_key: str, options: dict = None) -> S3:
        if s3_type == 'minio':
            logger.info("Creating Minio Service")
            from utils.s3.minio_service import MinioService
            return MinioService(host_url, access_key, secret_key, options)
        else:
            raise ValueError("Invalid S3 type")


