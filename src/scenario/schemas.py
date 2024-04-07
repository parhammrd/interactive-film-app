from pydantic import BaseModel
from typing import List, Optional


class InteractionItem(BaseModel):
    nextVideoId: Optional[int] = None
    text: Optional[str] = None


class Interaction(BaseModel):
    type: str
    title: Optional[str] = None
    items: List[InteractionItem]


class Video(BaseModel):
    id: int
    url: Optional[str] = None
    interactions: Interaction


class Chapter(BaseModel):
    id: int
    title: str
    videos: List[Video]


class ChapterList(BaseModel):
    chapters: List[Chapter]
