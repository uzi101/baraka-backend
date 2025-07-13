from fastapi import APIRouter, Depends
from app.services.auth_service import get_current_user

router = APIRouter()


@router.get("/me")
def get_me(user=Depends(get_current_user)):
    return {
        "uid": user.get("uid"),
        "email": user.get("email"),
        "provider": user.get("firebase", {}).get("sign_in_provider", "unknown")
    }
