# user: https://talibilat.medium.com/api-beginner-to-advance-building-user-registration-in-fastapi-73db80eed71f
from fastapi import FastAPI
from routers import item_router, post_router, user_router, root_router

# create routers
app = FastAPI()
app.include_router(root_router.router)
app.include_router(post_router.router, prefix='/post')
app.include_router(user_router.router, prefix='/user')
app.include_router(item_router.router, prefix='/item')

# create tables
from db.sqlalchemy_conn  import engine
from db.sqlalchemy_table import Base
Base.metadata.create_all(bind=engine)

