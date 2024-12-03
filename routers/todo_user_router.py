from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from starlette import status

from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from schemas import todo_schema
from db import sqlalchemy_crud, sqlalchemy_conn, sqlalchemy_table
from utils import auth, u_hash

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

templates = Jinja2Templates(directory='templates')
router = APIRouter()

@router.get('/t')
async def root(): return {"Test": "User! Step by Step a, FastAPI!"}


@router.get('/', response_class=HTMLResponse)
async def auth_page(request: Request):
    user = await auth.get_current_user(request)
    if user is not None:
        return RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    return templates.TemplateResponse('user/login.html', {'request': request})


@router.get('/register')
async def register_page(request: Request):
    # return {"User": "User! Step by Step a, FastAPI!"}
    user = await auth.get_current_user(request)
    if user is not None:
        return RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    return templates.TemplateResponse('user/register.html', {'request': request})


@router.post('/register')
async def create_new_user(request: Request, db: Session = Depends(sqlalchemy_conn.get_db)):
    form = todo_schema.RegisterForm(request)
    await form.create_register_form()
    user = sqlalchemy_table.TodoUsers()
    user.email = form.email
    user.username = form.username
    user.first_name = form.firstname
    user.last_name = form.lastname
    user.hashed_password = u_hash.hash_password(form.password)
    # user.phone_number = form.phonenumber
    user.is_active = True

    db.add(user)
    db.commit()

    msg = 'User successfully created'
    response = templates.TemplateResponse('user/login.html', {'request': request, 'msg': msg})
    return response


@router.post('/auth', response_class=HTMLResponse)
async def login(request: Request, db: Session = Depends(sqlalchemy_conn.get_db)):
    try:
        form = todo_schema.LoginForm(request)
        await form.create_oauth_form()
        response = RedirectResponse(url='/success', status_code=status.HTTP_302_FOUND)
        validate_user_cookie = await login_for_access_token(response=response, form_data=form, db=db)

        if not validate_user_cookie:
            msg = 'Incorrect Username or Password'
            return templates.TemplateResponse('user/login.html', {'request': request, 'msg': msg})
        return response
    except HTTPException:
        msg = 'Unknown Error'
        return templates.TemplateResponse('user/login.html', {'request': request, 'msg': msg})
    

@router.post('/token')
async def login_for_access_token(response: Response,
                                 form_data: OAuth2PasswordRequestForm = Depends(),
                                 db: Session = Depends(sqlalchemy_conn.get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)

    if not user:
        return False  # token_exception()

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username, 'id': user.id},
        expires_delta=access_token_expires)

    response.set_cookie(key='access_token', value=access_token, httponly=True)

    return True  # {"access_token": access_token, "token_type": "bearer"}


@router.get('/logout', response_class=HTMLResponse)
async def logout(request: Request):
    msg = 'Logout Successful'
    response = templates.TemplateResponse('user/login.html', {'request': request, 'msg': msg})
    response.delete_cookie(key='access_token')
    return response
