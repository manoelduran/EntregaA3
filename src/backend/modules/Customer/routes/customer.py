from fastapi import APIRouter

customerRouter = APIRouter()

@customerRouter.get("/customers/", tags=["customers"])
def index():
    return [{"username": "Rick"}, {"username": "Morty"}]