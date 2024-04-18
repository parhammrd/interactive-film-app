from decouple import config

from .dialogue.models import Dialogue
from .scenario.models import Scenario

from sqlmodel import SQLModel, create_engine

engine = create_engine(config('DATABASE_URL'))

SQLModel.metadata.create_all(engine)
