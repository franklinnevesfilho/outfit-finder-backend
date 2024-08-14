from franklin_fastapi_extension import FastAPI, register_routes
from logger import logger
import uvicorn
import routes
import os

app = FastAPI()

register_routes(app, routes)

host = os.getenv("HOST", "0.0.0.0")
port = int(os.getenv("PORT", 8000))


if __name__ == "__main__":
    logger.info("Starting application")
    uvicorn.run(app, host=host, port=port)
