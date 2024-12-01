# step 1. start
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Step by Step , FastAPI!"}


# step 2: sub route post
from routers.post_router import router
app.include_router(router, prefix='/post')