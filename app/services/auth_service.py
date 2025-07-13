from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.firebase import verify_firebase_token
from app.db.deps import get_db
from app.models.user import User

# Dependency: validates token and ensures user is in DB


def get_current_user(
    authorization: str = Header(...),
    db: Session = Depends(get_db)  # Injects a per-request DB session
) -> User:
    # Expect Authorization: Bearer <token>
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401, detail="Invalid auth header format")

    token = authorization.split(" ")[1]

    try:
        # 🔐 Step 1: Verify token with Firebase Admin SDK
        print("🔐 Verifying Firebase token...")
        firebase_data = verify_firebase_token(token)
        print("✅ Firebase token verified:", firebase_data)

        uid = firebase_data["uid"]
        email = firebase_data.get("email", "unknown@example.com")

        # 🧠 Step 2: Look up user in DB using Firebase UID
        user = db.query(User).filter(User.firebase_uid == uid).first()

        # 🆕 Step 3: If user doesn't exist, create them
        if not user:
            print("🆕 Creating new user:", uid, email)
            user = User(firebase_uid=uid, email=email)
            db.add(user)
            db.commit()
            db.refresh(user)
            print("✅ User inserted into DB")

        # 🔁 Step 4: Return the user (from DB, not raw Firebase dict)
        print("✅ Returning user:", user.email)
        return user

    except Exception as e:
        import traceback
        print("❌ Firebase auth flow failed:")
        traceback.print_exc()
        raise HTTPException(status_code=401, detail="Invalid Firebase token")
