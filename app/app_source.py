from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import Settings
from app.db import db_pg
from app.routers import router 
from app.utils.u_logger import logger_config
from app.seeds import mock_data_generator 

logger = logger_config(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_pg.create_db_and_tables()
    mock_data_generator.create_heroes_and_teams()

    logger.info("startup: triggered")

    yield

    logger.info("shutdown: triggered")


def create_app(settings: Settings):
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        docs_url="/",
        description=settings.DESCRIPTION,
        lifespan=lifespan,
    )

    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


    app.include_router(router)

    return app
