from typing import List, Optional
from app.models.product import Product
from app.repositories.product_repository import ProductRepository


class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def get_products(self) -> List[Product]:
        return self.repository.read_products()

    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        return self.repository.get_product_by_id(product_id)

    def get_products_by_attributes(self, **kwargs) -> List[Product]:
        return self.repository.get_products_by_attributes(**kwargs)

    def add_product(self, product: Product) -> None:
        self.repository.add_product(product)

    def update_product(self, product_id: int, updated_product: Product) -> None:
        self.repository.update_product(product_id, updated_product)

    def delete_product(self, product_id: int) -> None:
        self.repository.delete_product(product_id)