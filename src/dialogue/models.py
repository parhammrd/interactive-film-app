from typing import Optional
from sqlmodel import Field, SQLModel


class Dialogue(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    userid: Optional[str]
    question: str
    answer: Optional[str]
