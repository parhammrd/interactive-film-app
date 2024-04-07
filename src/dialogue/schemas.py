from pydantic import BaseModel, EmailStr
from typing import Optional


class UserResponse(BaseModel):
    email: Optional[EmailStr] = None
    question: str
    answer: Optional[str]
