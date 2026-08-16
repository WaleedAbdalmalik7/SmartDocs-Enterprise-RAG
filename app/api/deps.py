"""Common dependencies for API routes."""
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import Generator
from ..db.session import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")


def get_db_dep() -> Generator:
    yield from get_db()


def get_current_user(token: str = Depends(oauth2_scheme)):
    # Placeholder: decode token and fetch user
    if not token:
        raise HTTPException(status_code=401, detail="Missing token")
    return {"sub": "anonymous"}
