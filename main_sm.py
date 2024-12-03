from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from routers import item_router, post_router, user_router, root_router, todo_router, hero_router

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
app.include_router(hero_router.router, prefix='/hero')

# create tables
from db.sm_conn  import engine
from db.sm_table import SQLModel
SQLModel.metadata.create_all(bind=engine)

