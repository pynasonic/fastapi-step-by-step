from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from sqlalchemy.orm import Session

from schemas import todo_schema
from db import sqlalchemy_crud, sqlalchemy_conn, sqlalchemy_table
from . import todo_user_router

router = APIRouter()

@router.get('/')
async def root(): return {"message": "Todod! Step by Step a, FastAPI!"}

router.include_router(todo_user_router.router, prefix='/user')
