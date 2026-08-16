"""Auth endpoints (register, login)."""
from fastapi import APIRouter, Depends
from ..deps import get_db_dep
from ...schemas.schemas import UserCreate, Token

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=Token)
def register(user: UserCreate, db=Depends(get_db_dep)):
    # Implement registration logic
    return {"access_token": "dummy", "token_type": "bearer"}


@router.post("/token", response_model=Token)
def login():
    # Implement login and token creation
    return {"access_token": "dummy", "token_type": "bearer"}
