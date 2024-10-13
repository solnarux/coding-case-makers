from fastapi import Depends

from app.data.database import get_db
from app.repositories.json_product_repository import JSONProductRepository
from app.repositories.db_product_repository import DBProductRepository
from app.repositories.user_repository import UserRepository
from app.services.product_service import ProductService
from app.services.user_service import UserService


def get_product_service(db=Depends(get_db)) -> ProductService:
    # repository = JSONProductRepository()
    repository = DBProductRepository(db)
    return ProductService(repository)


def get_user_service(db=Depends(get_db)) -> UserService:
    repository = UserRepository(db)
    return UserService(repository)
