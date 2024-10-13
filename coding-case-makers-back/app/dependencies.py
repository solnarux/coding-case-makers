from fastapi import Depends

from app.data.database import get_db
from app.repositories.json_product_repository import JSONProductRepository
from app.repositories.db_product_repository import DBProductRepository
from app.services.product_service import ProductService


def get_product_service(db=Depends(get_db)) -> ProductService:
    repository = JSONProductRepository()
    #repository = DBProductRepository(db)
    return ProductService(repository)
