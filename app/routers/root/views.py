from fastapi import APIRouter

router = APIRouter()

@router.get('/test')
async def root(): return {"Mongo": "New View Step by Step a, FastAPI!"}
