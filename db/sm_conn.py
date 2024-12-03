from sqlmodel import Field, SQLModel, create_engine, Session

from . import sm_table

import dotenv
CFG = dotenv.dotenv_values("./.env")

engine = create_engine(CFG['SQLALCHEMY_DATABASE_URL'], echo=True)
session = Session(engine)


