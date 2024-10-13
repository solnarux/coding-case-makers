from pydantic import BaseModel


class Product(BaseModel):
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
    category: str
