from pydantic_settings import BaseSettings
from typing import Optional
class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    GOOGLE_CLIENT_ID: Optional[str]= None
    CHROME_DRIVER_PATH: str = "./chroma_db"
    STORAGE_PATH: str = "./storage"
    class Config:
        env_file = ".env"
settings = Settings()
