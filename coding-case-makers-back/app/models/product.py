from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, index=True)
    model = Column(String)
    processor = Column(String)
    ram = Column(Integer)
    storage = Column(Integer)
    price = Column(Float)
    description = Column(String)
    stars = Column(Float)
    stock = Column(Integer)
    category = Column(String)
