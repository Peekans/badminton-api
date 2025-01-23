from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

db_url = os.getenv("DATABASE_URL", "sqlite:///./badminton.db")

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)

Base = declarative_base()