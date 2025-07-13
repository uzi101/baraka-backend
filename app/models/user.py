from sqlalchemy import Column, Integer, String, DateTime, Numeric, func
from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firebase_uid = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    stripe_customer_id = Column(String, nullable=True)
    roundup_total = Column(Numeric, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
