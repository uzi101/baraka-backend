from fastapi import APIRouter, Depends, Header, HTTPException
from app.core.firebase import verify_token

router = APIRouter()

def get_current_user(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid auth header")

    id_token = authorization.split(" ")[1]
    decoded = verify_token(id_token)
    return decoded

@router.get("/me")
def get_my_profile(user = Depends(get_current_user)):
    return {"email": user["email"], "uid": user["uid"]}
