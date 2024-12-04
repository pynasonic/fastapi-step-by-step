from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from app.config import Settings
from app.routers import router 
from app.utils.u_logger import logger_config

logger = logger_config(__name__)

logger.info("starting...")

class AutoPassAuthMiddleware(BaseHTTPMiddleware):
    # async def dispatch(self, request: Request, call_next):
    #     # Check for Authorization header
    #     if "Authorization" not in request.headers:
    #         # Add dummy auth header for testing purposes
    #         request.headers.__dict__["_list"].append(
    #             (b"authorization", b"Basic svc_test:superstrongpassword")
    #         )

    #     response = await call_next(request)
    #     return response
    async def dispatch(self, request: Request, call_next):
        # Simulate authentication by adding a fake user to the request state
        request.state.user = {"username": "svc_test", "password": "superstrongpassword"}

        response = await call_next(request)
        return response


def create_app(settings: Settings):
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        docs_url="/",
        description=settings.DESCRIPTION,
    )

    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_middleware(AutoPassAuthMiddleware)

    app.include_router(router)

    return app
