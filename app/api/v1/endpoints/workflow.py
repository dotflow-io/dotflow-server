"""Workflow endpoint"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/workflow", status_code=200)
async def get():
    return []


@router.get("/workflow/{id}", status_code=200)
def get_by_id(id: int):
    return {}


@router.post("/workflow", status_code=201)
async def post():
    return {}
