import sqlalchemy
from sqlmodel import Field, SQLModel


class Scenario(SQLModel, table=True):
    id: int = Field(primary_key=True)
    chapterlist: dict = Field(sa_type=sqlalchemy.types.JSON)
