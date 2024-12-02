from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException

from seed_data.storage_in_memory import my_posts
from schemas import t_schema, user_schema
from db import sqlalchemy_crud, sqlalchemy_conn, sqlalchemy_table
from utils import u_hash

router = APIRouter()

@router.get('/posts')
async def index(): return my_posts


@router.get("/", response_model=list[t_schema.Item])
async def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(sqlalchemy_conn.get_db)):
    items = sqlalchemy_crud.get_items(db, skip=skip, limit=limit)
    return items


@router.get("/{item_id}", response_model=t_schema.Item)
def read_item(item_id: int, db: Session = Depends(sqlalchemy_conn.get_db)):
    db_item = sqlalchemy_crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.post("/new/", response_model=user_schema.UserOut, status_code=201)
def create_user(user: user_schema.UserCreate, db: Session = Depends(sqlalchemy_conn.get_db)):
    hashed_password = u_hash.hash_password(user.password)
    new_user = sqlalchemy_table.User(email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

