import firebase_admin
from firebase_admin import credentials, auth
from pathlib import Path

# Load the service account JSON from root
cred_path = Path("firebase_service_account.json")

if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)


def verify_firebase_token(id_token: str) -> dict:
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception as e:
        raise ValueError("Invalid Firebase token")  # FastAPI will handle error
