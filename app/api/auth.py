from fastapi import APIRouter, Depends
from app.services.auth_service import get_current_user
from app.models.user import User
from app.schemas.user_schema import UserOut

router = APIRouter()


@router.get("/me", response_model=UserOut)
def get_me(user: User = Depends(get_current_user)):
    return user  # No need to manually serialize anything!
