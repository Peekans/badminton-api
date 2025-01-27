from fastapi import FastAPI
from app.api import endpoints
from app.database.database import engine, Base

app = FastAPI(
    title="Badminton Racket API",
    description="API that collects, sorts, and sectionalizes racket data",
    version="1.0.0"
)

app.include_router(endpoints.router)

Base.metadata.create_all(bind=engine)