from typing import List, Optional, Any

from sqlalchemy import Row

from app.models.product import Product


class ProductRepository:
    def read_products(self) -> List[Product]:
        """Read all products from storage."""
        raise NotImplementedError

    def write_products(self, products: List[Product]) -> None:
        """Write a list of products to storage."""
        raise NotImplementedError

    def add_product(self, product: Product) -> None:
        """Add a new product to storage."""
        raise NotImplementedError

    def update_product(self, product_id: int, updated_product: Product) -> None:
        """Update an existing product in storage."""
        raise NotImplementedError

    def delete_product(self, product_id: int) -> None:
        """Delete a product from storage."""
        raise NotImplementedError

    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        """Retrieve a product by ID from storage."""
        raise NotImplementedError

    def get_products_by_attributes(self, attributes) -> List[Product]:
        """Retrieve products filtered by attributes."""
        raise NotImplementedError

    def get_products_by_brand(self) -> list[Row[tuple[Any, Any, Any]]]:
        """Retrieve products by brand"""
        raise NotImplementedError