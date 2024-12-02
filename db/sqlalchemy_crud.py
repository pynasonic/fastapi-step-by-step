from sqlalchemy.orm import Session
from . import sqlalchemy_conn, sqlalchemy_table
from schemas import t_schema

def get_item(db: Session, item_id: int):
    return db.query(sqlalchemy_table.Item).filter(sqlalchemy_table.Item.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(sqlalchemy_table.Item).offset(skip).limit(limit).all()

def create_item(db: Session, item: t_schema.ItemCreate):
    db_item = sqlalchemy_table.Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item