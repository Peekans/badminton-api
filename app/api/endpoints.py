from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.models import Racket
from app.database.database import get_db
from app.schemas.schemas import RacketSchema, RacketCreateSchema

router = APIRouter()