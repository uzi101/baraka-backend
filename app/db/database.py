from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
import os
print("🧨 ENV[DATABASE_URL] from os.environ =", os.environ.get("DATABASE_URL"))
print("⚠️  DATABASE_URL from settings:", settings.DATABASE_URL)

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
