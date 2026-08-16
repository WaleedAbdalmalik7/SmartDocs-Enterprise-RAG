"""SQLAlchemy base and example models."""
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Define your models here or import them so Alembic detects them.
# Example:
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True, nullable=False)
