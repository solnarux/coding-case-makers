from pydantic import BaseModel

class ProductBase(BaseModel):
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

    class Config:
        from_attributes = True


