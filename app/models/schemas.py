from pydantic import BaseModel, Field

class ItemIn(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    price: float

class ItemOut(BaseModel):
    id: int
    name: str
    price: float