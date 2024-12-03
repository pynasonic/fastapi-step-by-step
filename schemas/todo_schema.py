from typing import Optional
from fastapi import Request
from pydantic import BaseModel, Field

class UserVerification(BaseModel):
    username: str
    password: str
    new_password: str


class PhoneNumber(BaseModel):
    phone_number: str


class Todo(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(gt=0, lt=6, description='The priority must be between 1-5')
    complete: bool


class CreateUser(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str
    phone_number: Optional[str]

class LoginForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.username: Optional[str] = None
        self.password: Optional[str] = None

    async def create_oauth_form(self):
        form = await self.request.form()
        self.username = form.get('email')
        self.password = form.get('password')


class RegisterForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.email: Optional[str] = None
        self.username: Optional[str] = None
        self.password: Optional[str] = None
        self.password2: Optional[str] = None
        self.firstname: Optional[str] = None
        self.lastname: Optional[str] = None

    async def create_register_form(self):
        form = await self.request.form()
        self.email = form.get('email')
        self.username = form.get('username')
        self.password = form.get('password')
        self.password2 = form.get('password2')
        self.firstname = form.get('firstname')
        self.lastname = form.get('lastname')