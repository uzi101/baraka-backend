from fastapi import Header, HTTPException, Depends
from app.core.firebase import verify_firebase_token

# Dependency that extracts and verifies the token


def get_current_user(authorization: str = Header(...)) -> dict:
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401, detail="Invalid auth header format")

    token = authorization.split(" ")[1]

    try:
        user_data = verify_firebase_token(token)
        return user_data
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid Firebase token")
