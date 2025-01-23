from pydantic import BaseModel

class RacketBase(BaseModel):
    brand: str
    name: str
    frame = str
    shaft = str
    flex = str
    Weight = float
    max_tension = int
    length = float
    balance = str
    grommets = int
    shaft_diameter = float
    special_features = str

class RacketCreateSchema(RacketBase):
    pass

class RacketSchema(RacketBase):
    id: int

    class Config:
        orm_mode = True