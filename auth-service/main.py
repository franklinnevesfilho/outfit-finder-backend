from logger import logger
from fastapi import FastAPI

app = FastAPI()

"""
User Registration:

POST /register: Endpoint for creating a new user account. This would include handling user input like username, email, password, etc.
POST /register/verify: (Optional) Endpoint for verifying a new user account via email or phone number.
"""
@app.post("/register")
async def register_user():
    logger.info("Registering a new user")
    pass

@app.post("/register/verify")
async def verify_user():
    logger.info("Verifying a new user")
    pass
"""
User Login:

POST /login: Endpoint for authenticating a user with a username/email and password. This would return a JWT token or similar.
Token Management:
"""
@app.post("/login")
async def login_user():
    logger.info("Logging in a user")
    pass

"""

POST /token/refresh: Endpoint for refreshing an access token using a refresh token.
POST /token/revoke: Endpoint for revoking a token, effectively logging out the user.
Password Management:
"""
@app.post("/token/refresh")
async def refresh_token():
    logger.info("Refreshing a token")
    pass

@app.post("/token/revoke")
async def revoke_token():
    logger.info("Revoking a token")
    pass


"""
POST /password/reset/request: Endpoint to initiate a password reset request. Typically sends an email with a reset link or token.
POST /password/reset/confirm: Endpoint to confirm and apply a new password using the reset token.
"""
@app.post("/password/reset/request")
async def request_password_reset():
    logger.info("Requesting password reset")
    pass

@app.post("/password/reset/confirm")
async def confirm_password_reset():
    logger.info("Confirming password reset")
    pass

"""
User Profile:

GET /me: Endpoint to retrieve the authenticated user's profile information.
PATCH /me: Endpoint to update the authenticated user's profile information (e.g., email, username, etc.).
"""
@app.get("/me")
async def get_user_profile():
    logger.info("Getting user profile")
    pass

@app.patch("/me")
async def update_user_profile():
    logger.info("Updating user profile")
    pass


"""
Authorization:

GET /roles: Endpoint to retrieve roles/permissions for the authenticated user.
POST /roles/assign: Endpoint to assign roles or permissions to a user (typically admin level).
Account Deactivation/Deletion:
"""
@app.get("/roles")
async def get_roles():
    logger.info("Getting user roles")
    pass

@app.post("/roles/assign")
async def assign_roles():
    logger.info("Assigning roles")
    pass


"""
POST /deactivate: Endpoint to deactivate the user's account.
DELETE /delete: Endpoint to permanently delete the user's account.
"""
@app.post("/deactivate")
async def deactivate_account():
    logger.info("Deactivating account")
    pass

@app.delete("/delete")
async def delete_account():
    logger.info("Deleting account")
    pass


"""
Social Login (Optional):

POST /social/{provider}/login: Endpoint to log in using third-party providers like Google, Facebook, etc.
Two-Factor Authentication (Optional):
"""
@app.post("/social/{provider}/login")
async def social_login(provider: str):
    logger.info(f"Logging in with {provider}")
    pass

"""
POST /2fa/setup: Endpoint to set up two-factor authentication for a user.
POST /2fa/verify: Endpoint to verify the 2FA code during login.
POST /2fa/disable: Endpoint to disable 2FA for a user.
"""

@app.post("/2fa/setup")
async def setup_2fa():
    logger.info("Setting up 2FA")
    pass

@app.post("/2fa/verify")
async def verify_2fa():
    logger.info("Verifying 2FA")
    pass

@app.post("/2fa/disable")
async def disable_2fa():
    logger.info("Disabling 2FA")
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
