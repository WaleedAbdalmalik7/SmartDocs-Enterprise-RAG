"""Pydantic request/response schemas."""
from pydantic import BaseModel, Field
from typing import Optional


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserCreate(BaseModel):
    email: str
    password: str


class UserOut(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True


class DocumentCreate(BaseModel):
    title: str
    description: Optional[str] = None


class DocumentOut(BaseModel):
    id: str
    title: str
    description: Optional[str] = None

    class Config:
        orm_mode = True
