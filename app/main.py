from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import root, auth  # this imports your first route
from app.core.config import settings  # loads env config


print("📦 DATABASE_URL:", settings.DATABASE_URL)

app = FastAPI(
    title="Baraka API",
    version="0.1.0",
    docs_url="/docs",         # Swagger UI
    redoc_url="/redoc",       # ReDoc docs (optional)
)

# Allow frontend to connect (Vercel, localhost, etc.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production: ["https://baraka.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount route groups
app.include_router(root.router, prefix="/api")
app.include_router(auth.router, prefix="/api/auth")

# In production, you'll add more routes:
# e.g. app.include_router(auth.router, prefix="/api/auth")
