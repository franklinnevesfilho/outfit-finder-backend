from franklin_fastapi_extension import FastAPI, request, Query, register_routes
from logger import logger
from services import auth_service
from dto import UserRegistration, UserLogin
import uvicorn
import routes
import os

app = FastAPI()

@app.post("/register")
async def register_user(user: Query):
    logger.info("Registering a user")
    return await request.call(auth_service.register_user, user, UserRegistration)

@app.post("/login")
async def login_user(user: Query):
    logger.info("Logging in a user")
    return await request.call(auth_service.login_user, user, UserLogin)


@app.post("/social/{provider}/login")
async def social_login(provider: str):
    logger.info(f"Logging in with {provider}")
    return {"message": f"Logged in with {provider}"}



register_routes(app, routes)

host = os.getenv("HOST", "0.0.0.0")
port = int(os.getenv("PORT", 8000))


if __name__ == "__main__":
    logger.info("Starting application")
    uvicorn.run(app, host=host, port=port)
