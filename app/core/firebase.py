import firebase_admin
from firebase_admin import credentials, auth
from fastapi import HTTPException

cred = credentials.Certificate("firebase_service_account.json")
firebase_admin.initialize_app(cred)

def verify_token(id_token: str):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token  # contains uid, email, etc.
    except Exception as e:
        print("Token verification failed:", e)
        raise HTTPException(status_code=401, detail="Invalid or expired token")
