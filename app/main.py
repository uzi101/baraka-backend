from fastapi import FastAPI
from app.routes import root

app = FastAPI()

app.include_router(root.router)

@app.get("/health")
def health_check():
    return {"status": "Baraka backend is running"}
