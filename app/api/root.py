from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def healthcheck():
    return {"message": "Baraka backend is alive"}
