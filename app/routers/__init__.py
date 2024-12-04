from fastapi import APIRouter, Depends

from app.auth import authent
from app.routers.todo   import views as todo
from app.routers.root   import views as root

router = APIRouter()

router.include_router(
    root.router,    tags=["Root"],    dependencies=[Depends(authent)],
)
router.include_router(
    todo.router,    prefix="/todo",    tags=["Todo"],    dependencies=[Depends(authent)],
)
