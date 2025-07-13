from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    FIREBASE_PROJECT_ID: str
    STRIPE_SECRET_KEY: str
    PLAID_CLIENT_ID: str
    PLAID_SECRET: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"


# pyright: reportCallIssue=false
settings = Settings()
