from sqlmodel import Field, SQLModel, create_engine

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None
    team_id: int | None = Field(default=None, foreign_key="hero_team.id")
    
class Hero_Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str
