from sqlalchemy import Column, Integer, String, TIMESTAMP, text, Boolean, ForeignKey, Double
from sqlalchemy.orm import relationship

from db.sqlalchemy_conn import Base

# todo
class TodoUsers(Base):
    __tablename__ = "todo_users"

    id          = Column(Integer, primary_key=True, index=True)
    email       = Column(String(200), unique=True, index=True)
    username    = Column(String(200), unique=True, index=True)
    first_name  = Column(String(200))
    last_name   = Column(String(225))
    hashed_password = Column(String(225))
    is_active   = Column(Boolean, default=True)
    phone_number= Column(String(225))
    address_id  = Column(Integer, ForeignKey('todo_address.id'), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)    

    todos   = relationship('TodoTodos', back_populates='owner')
    address = relationship('TodoAddress', back_populates='user_address')


class TodoTodos(Base):
    __tablename__ = 'todo_todos'

    id      = Column(Integer, primary_key=True, index=True)
    title   = Column(String(225))
    amount  = Column(Double)
    description = Column(String(225))
    owner_id = Column(Integer, ForeignKey('todo_users.id'))
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)    

    owner = relationship('TodoUsers', back_populates='todos')


class TodoAddress(Base):
    __tablename__ = 'todo_address'

    id      = Column(Integer, primary_key=True, index=True)
    apt_num = Column(Integer)  # alembic
    address1= Column(String(255))
    address2= Column(String(255))
    city    = Column(String(255))
    state = Column(String(255))
    country = Column(String(255))
    postalcode = Column(String(255))
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)    

    user_address = relationship('TodoUsers', back_populates='address')

# todo    


class TUser(Base):
    __tablename__ = "t_users"

    id      = Column(Integer, primary_key=True, index=True)
    email   = Column(String, unique=True, nullable=False)
    password= Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)    
    
class TItem(Base):
    __tablename__ = "t_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)