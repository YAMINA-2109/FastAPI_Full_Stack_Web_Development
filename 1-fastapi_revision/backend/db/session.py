from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from typing import Generator

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print(f"Database URL: {SQLALCHEMY_DATABASE_URL}")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SESSIONLOCAL = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# sqlite
# SQLALCHEMY_DATABASE_URL_SQLITE = "sqlite:///./sql_app.db"
# engine_sqlite = create_engine(
#     SQLALCHEMY_DATABASE_URL_SQLITE, connect_args={"check_same_thread": False}
# )

def get_db() -> Generator:
    try:
        db = SESSIONLOCAL()
        yield db
    finally:
        db.close()