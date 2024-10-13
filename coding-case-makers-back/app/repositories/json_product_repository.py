import json
from typing import List, Optional
from app.models.product import Product
from app.repositories.product_repository import ProductRepository


class JSONProductRepository(ProductRepository):
    JSON_FILE_PATH = 'app/data/products.json'

    def read_products(self, **kwargs) -> List[Product]:
        """Read products from JSON file and filter based on provided attributes."""
        with open(self.JSON_FILE_PATH, 'r') as file:
            products_data = json.load(file)
            filtered_products = []

            for data in products_data:
                product = Product(**data)
                match = True

                for key, value in kwargs.items():
                    if key in ['min_price', 'max_price']:
                        if key == 'min_price' and product.price < value:
                            match = False
                            break
                        if key == 'max_price' and product.price > value:
                            match = False
                            break
                    elif getattr(product, key, None) != value:
                        match = False
                        break

                if match:
                    filtered_products.append(product)

            return filtered_products

    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        products = self.read_products()
        for product in products:
            if product.id == product_id:
                return product
        return None

    def get_products_by_attributes(self, **kwargs) -> List[Product]:
        products = self.read_products()
        filtered_products = products

        for key, value in kwargs.items():
            filtered_products = [prod for prod in filtered_products if getattr(prod, key, None) == value]

        return filtered_products

    def write_products(self, products: List[Product]) -> None:
        with open(self.JSON_FILE_PATH, 'w') as file:
            json.dump([prod.model_dump() for prod in products], file, indent=4)

    def add_product(self, product: Product) -> None:
        products = self.read_products()
        products.append(product)
        self.write_products(products)

    def update_product(self, product_id: int, updated_product: Product) -> None:
        products = self.read_products()
        for index, product in enumerate(products):
            if product.id == product_id:
                products[index] = updated_product
                break
        self.write_products(products)

    def delete_product(self, product_id: int) -> None:
        products = self.read_products()
        products = [product for product in products if product.id != product_id]
        self.write_products(products)