from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette import status

from sqlalchemy.orm import Session

from schemas import todo_schema
from db import sqlalchemy_crud, sqlalchemy_conn, sqlalchemy_table
from utils import auth
from . import todo_user_router

templates = Jinja2Templates(directory='templates')

router = APIRouter()

@router.get('/t')
async def root(): return {"message": "Todod! Step by Step a, FastAPI!"}


@router.get('/', response_class=HTMLResponse)
async def read_all_by_user(request: Request,
                           db: Session = Depends(sqlalchemy_conn.get_db)):
    user = await auth.get_current_user(request)
    if user is None:
        return RedirectResponse(url='/auth', status_code=status.HTTP_302_FOUND)

    todos = (db.query(sqlalchemy_table.TodoTodos)
             .filter(sqlalchemy_table.TodoTodos.owner_id == user.get('id'))
             .order_by(sqlalchemy_table.TodoTodos.id).all())
    return templates.TemplateResponse('todo/home.html', {'request': request, 'todos': todos, 'user': user})


@router.get('/add-todo', response_class=HTMLResponse)
async def add_new_todo(request: Request):
    user = await auth.get_current_user(request)
    if user is None:
        return RedirectResponse(url='/auth', status_code=status.HTTP_302_FOUND)

    return templates.TemplateResponse('todo/add_todo.html', {'request': request, 'user': user})


@router.post('/add-todo', response_class=HTMLResponse)
async def create_todo_commit(request: Request,
                             title: str = Form(...),
                             description: str = Form(...),
                             priority: int = Form(...),
                             db: Session = Depends(sqlalchemy_conn.get_db)):
    user = await auth.get_current_user(request)
    if user is None:
        return RedirectResponse(url='/auth', status_code=status.HTTP_302_FOUND)

    todo_model = sqlalchemy_table.TodoTodos()
    todo_model.title = title
    todo_model.description = description
    todo_model.priority = priority
    todo_model.complete = False
    todo_model.owner_id = user.get('id')
    # print(todo_model.__dict__)
    # for i in range(1, 40):
    #     tm = models.Todos()
    #     tm.title = f"Todo {i}"
    #     tm.description = f"Todo description {i}"
    #     tm.priority = 1 if i % 2 == 0 else 4
    #     tm.complete = False if i % 2 == 0 else True
    #     tm.owner_id = user.get('id')
    #     db.add(tm)
    #     db.commit()
    db.add(todo_model)
    db.commit()

    return RedirectResponse(url='/todo', status_code=status.HTTP_302_FOUND)


router.include_router(todo_user_router.router, prefix='/user')
