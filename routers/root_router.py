from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def root(): return {"message": "Step by Step a, FastAPI!"}

@router.get('/success')
async def root(): return {"message": "Login success"}
