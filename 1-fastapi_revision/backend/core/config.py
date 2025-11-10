import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / ".env"
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME: str = "My FastAPI Application"
    PROJECT_VERSION: str = "0.1.0"

    POSTEGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTEGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTEGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTEGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")
    POSTEGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL: str = f"postgresql://{POSTEGRES_USER}:{POSTEGRES_PASSWORD}@{POSTEGRES_SERVER}:{POSTEGRES_PORT}/{POSTEGRES_DB}"

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

settings = Settings()