import os

#  Database configuration
DATABASE_HOST = os.getenv('DB_HOST', 'localhost')
DATABASE_PORT = os.getenv('DB_PORT', '3308')
DATABASE_USER = os.getenv('DB_USER', 'root')
DATABASE_PASSWORD = os.getenv('DB_PASSWORD', 'rootpassword')
DATABASE_NAME = os.getenv('DB_NAME', 'outfit_finder')

# S3 configuration
S3_HOST = os.getenv('S3_HOST', 'localhost')
S3_PORT = os.getenv('S3_PORT', '9000')
S3_ACCESS_KEY = os.getenv('S3_ACCESS_KEY', 'minioadmin')
S3_SECRET_KEY = os.getenv('S3_SECRET_KEY', 'minioadminpassword')
S3_SECURE = os.getenv('S3_SECURE', 'False')

# JWT configuration
JWT_SECRET = os.getenv('JWT_SECRET', 'secret')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS256')
JWT_EXPIRATION = os.getenv('JWT_EXPIRATION', 3600)

# FastAPI configuration
API_HOST = os.getenv('API_HOST', 'localhost')
API_PORT = os.getenv('API_PORT', 8000)
API_DEBUG = os.getenv('API_DEBUG', False)
API_RELOAD = os.getenv('API_RELOAD', False)

