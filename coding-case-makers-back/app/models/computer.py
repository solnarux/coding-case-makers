from pydantic import BaseModel

class Computer(BaseModel):
    id: int
    brand: str
    model: str
    processor: str
    ram: int
    storage: int
    price: float
    description: str
    stars: float
    stock: int


