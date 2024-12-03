from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from routers import item_router, post_router, user_router, root_router, todo_router

# create routers
app = FastAPI(
    description="Smart Accounting System",
    title="xAI API",
    version="1.1.1",
    contact={
        "name": "Data",
        "url": "http://receiptcanada.com",
    },
    swagger_ui_parameters={
        "syntaxHighlight.theme": "monokai",
        "layout": "BaseLayout",
        "filter": True,
        "tryItOutEnabled": True,
        "onComplete": "Ok"
    },
)

app.mount('/static', StaticFiles(directory='static'), name='static')
app.include_router(root_router.router)
app.include_router(post_router.router, prefix='/post')
app.include_router(user_router.router, prefix='/user')
app.include_router(item_router.router, prefix='/item')
app.include_router(todo_router.router, prefix='/todo')

# create tables
from db.sqlalchemy_conn  import engine
from db.sqlalchemy_table import Base
Base.metadata.create_all(bind=engine)

