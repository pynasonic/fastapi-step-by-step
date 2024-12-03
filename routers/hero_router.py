from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException

from seed_data.storage_in_memory import my_posts
from schemas import t_schema
from db import sqlalchemy_crud, sqlalchemy_conn

from db.sm_crud import create_heroes

router = APIRouter()

@router.get('/t')
async def index(): return my_posts


@router.get("/create_heros")
async def do():
    create_heroes()