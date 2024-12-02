from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from db.sqlalchemy_conn import Base

class User(Base):
    __tablename__ = "t_users"

    id      = Column(Integer, primary_key=True, index=True)
    email   = Column(String, unique=True, nullable=False)
    password= Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)    
    
class Item(Base):
    __tablename__ = "t_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)