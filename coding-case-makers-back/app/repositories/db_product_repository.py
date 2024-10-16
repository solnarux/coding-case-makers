from typing import List, Optional, Type, Tuple, Any

from sqlalchemy import and_, func, Row
from sqlalchemy.orm import Session

from app.models.product import Product
from app.repositories.product_repository import ProductRepository


class DBProductRepository(ProductRepository):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def read_products(self, **kwargs) -> List[Type[Product]]:
        """Read products from the database and filter based on provided attributes."""
        query = self.db_session.query(Product)

        filters = []

        for key, value in kwargs.items():
            if key == 'min_price':
                filters.append(Product.price >= value)
            elif key == 'max_price':
                filters.append(Product.price <= value)
            elif hasattr(Product, key):
                filters.append(getattr(Product, key) == value)

        if filters:
            query = query.filter(and_(*filters))

        return query.all()

    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        return self.db_session.query(Product).get(product_id)

    def write_products(self, products: List[Product]) -> None:
        for product in products:
            self.db_session.add(product)
        self.db_session.commit()

    def add_product(self, product: Product) -> None:
        self.db_session.add(product)
        self.db_session.commit()

    def update_product(self, product_id: int, updated_product: Product) -> None:
        product = self.db_session.query(Product).get(product_id)
        if product:
            for key, value in updated_product.dict().items():
                setattr(product, key, value)
            self.db_session.commit()

    def delete_product(self, product_id: int) -> None:
        product = self.db_session.query(Product).get(product_id)
        if product:
            self.db_session.delete(product)
            self.db_session.commit()

    def get_products_by_brand(self) -> list[Row[tuple[Any, Any, Any]]]:
        """Return a list of tuples containing brand name, total count, and total stock by brand."""
        return (
            self.db_session.query(
                Product.brand,
                func.count(Product.id).label('total_count'),
                func.sum(Product.stock).label('total_stock')
            )
            .group_by(Product.brand)
            .all()
        )

    def count_products(self) -> int:
        """Return the total number of products in the database."""
        return self.db_session.query(func.count(Product.id)).scalar()

    def get_stock_info(self) -> list[Row[tuple[Any, Any]]]:
        """Return a list of tuples containing product ID and current stock."""
        return self.db_session.query(Product.id, Product.stock).all()