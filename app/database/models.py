from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Racket(Base):
    __tablename__ = "rackets"
    
    id = Column(String, primary_key=True)
    brand = Column(String)
    name = Column(String)
    frame = Column(String)
    shaft = Column(String)
    flex = Column(String)
    Weight = Column(String)
    max_tension = Column(Integer)
    length = Column(Integer)
    balance = Column(String)
    grommets = Column(Integer)
    shaft_diameter = Column(Float)
    special_features = Column(String)