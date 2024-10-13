from typing import List, Optional, Tuple
from app.models.product import Product as ProductModel
from app.schemas.product import ProductBase
from app.repositories.product_repository import ProductRepository


class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def get_products(self) -> List[ProductBase]:
        products = self.repository.read_products()  # This returns List[ProductModel]
        return [self._convert_to_schema(product) for product in products]

    def get_product_by_id(self, product_id: int) -> Optional[ProductBase]:
        product = self.repository.get_product_by_id(product_id)  # Returns ProductModel or None
        return self._convert_to_schema(product) if product else None

    def get_products_by_attributes(self, **kwargs) -> List[ProductBase]:
        products = self.repository.read_products(**kwargs)  # Assuming this method is used for filtering
        return [self._convert_to_schema(product) for product in products]

    def add_product(self, product: ProductBase) -> ProductBase:
        product_model = self._convert_to_model(product)
        new_product = self.repository.add_product(product_model)
        return self._convert_to_schema(new_product)

    def update_product(self, product_id: int, updated_product: ProductBase) -> Optional[ProductBase]:
        product_model = self._convert_to_model(updated_product)  # Convert Pydantic to SQLAlchemy model
        updated_product_model = self.repository.update_product(product_id, product_model)
        return self._convert_to_schema(updated_product_model) if updated_product_model else None

    def delete_product(self, product_id: int) -> None:
        self.repository.delete_product(product_id)

    def get_product_count(self) -> int:
        """Get the total number of products."""
        return self.repository.count_products()

    def get_stock_info(self) -> Tuple[int, int]:
        """Get the current stock and out-of-stock counts."""
        stock_info = self.repository.get_stock_info()  # This returns a list of tuples (id, stock)
        total_stock = sum(stock for _, stock in stock_info)
        out_of_stock_count = sum(100 - stock for _, stock in stock_info)
        return total_stock, out_of_stock_count

    def _convert_to_schema(self, product: ProductModel) -> ProductBase:
        """Convert SQLAlchemy Product model to Pydantic ProductBase schema."""
        return ProductBase.from_orm(product)

    def _convert_to_model(self, product: ProductBase) -> ProductModel:
        """Convert Pydantic ProductBase schema to SQLAlchemy Product model."""
        return ProductModel(**product.dict())