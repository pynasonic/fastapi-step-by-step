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

3. SQLAlchemy

It’s important to note that SQLAlchemy by itself doesn’t know how to talk to a database directly. It requires a database driver to handle the communication with the database. Since we are using PostgreSQL, we’ve already installed the necessary driver (psycopg2) in previous sections.

    - pip install sqlalchemy
    - pip install psycopg2

3.1 Create db folder to hold all the database connection and operation.
3.2 the first step is to connect to database. create conn_sqlalchemy.py.
3.3 save db.uri into .env
3.4 engine
3.5 session
3.6 base table

