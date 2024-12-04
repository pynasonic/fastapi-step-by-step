import uvicorn

from app import mongo as app
from app.config import settings

api = app.create_app(settings)

if __name__ == "__main__":
    uvicorn.run("asgi:api", host="0.0.0.0", port=8080, reload=True)
