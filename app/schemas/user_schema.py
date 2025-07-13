from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserOut(BaseModel):
    id: int
    firebase_uid: str
    email: str
    roundup_total: float
    stripe_customer_id: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True  # Allows Pydantic to read from SQLAlchemy model instances
