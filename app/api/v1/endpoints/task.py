"""Task endpoint"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/task", status_code=200)
async def get():
    return []


@router.get("/task/{id}", status_code=200)
def get_by_id(id: int):
    return {}


@router.post("/task", status_code=201)
async def post():
    return {}
