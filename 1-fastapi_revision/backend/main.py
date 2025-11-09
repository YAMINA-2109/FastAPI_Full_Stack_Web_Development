from fastapi import FastAPI
from core.config import settings
from db.session import engine
import db.base
from db.base_class import Base
from apis.base import api_router


def include_router(app):
    app.include_router(api_router)


def create_tables():
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    return app

app = start_application()

@app.get("/")
def home_page():
    return {"message": "Welcome to My FastAPI Application!"}   
