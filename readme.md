Step by step, we will cover all the aspects of the FastAPI. For each step, there will be a branch for it. Just checkout the branch matching your level, you will step by step move to the upper level of the FastAPI.

1. Start 

Prepare the environment:
    Install Python (3.12.4)
    py -m venv .v12
    create .vscode\settings.json (refer the file in the repository)
    create .gitignore (or download from this repository)
    .v12\scripts\activate
    pip install fastapi
    pip install uvicorn
    compose or copy main.py
    uvicorn main:app --reload

2. In Memory Data

Create storage_in_memory.py to store the data. 
Create ./routers to save routers. First router is post_router.py
Link Post router to root router in main.py.
http://127.0.0.1:8000/post/ will show the data in storage_in_memory.py


