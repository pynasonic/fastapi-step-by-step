import os
import secrets
from typing import ClassVar, Literal
from pydantic_settings import BaseSettings

from dotenv import dotenv_values

class Settings(BaseSettings):
    PROJECT_NAME: str = f"SQLModel API - {os.getenv('ENV', 'development').capitalize()}"
    DESCRIPTION: str = "A FastAPI + SQLModel production-ready API"
    ENV: Literal["development", "staging", "production"] = "development"
    VERSION: str = "1.1.2"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    CFG: ClassVar  = dotenv_values(".env")
    API_USERNAME: str = "svc_test"
    API_PASSWORD: str = "superstrongpassword"

    class Config:
        case_sensitive = True


settings = Settings()


class TestSettings(Settings):
    class Config:
        case_sensitive = True


test_settings = TestSettings()
