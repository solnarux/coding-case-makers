# app/routes/product_routes.py

from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from app.models.product import Product as ProductModel  # SQLAlchemy model
from app.schemas.product import ProductBase  # Pydantic schema
from app.services.product_service import ProductService
from app.dependencies import get_product_service

router = APIRouter()

@router.get("/products", response_model=List[ProductBase])
async def get_products(
        brand: Optional[str] = None,
        model: Optional[str] = None,
        processor: Optional[str] = None,
        storage: Optional[int] = None,
        ram: Optional[int] = None,
        stars: Optional[float] = None,
        stock: Optional[int] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        category: Optional[str] = None,
        service: ProductService = Depends(get_product_service)
):
    """Get a list of all products, optionally filtered by various attributes."""
    filters = {}
    if brand:
        filters['brand'] = brand
    if model:
        filters['model'] = model
    if storage:
        filters['storage'] = storage
    if processor:
        filters['processor'] = processor
    if ram:
        filters['ram'] = ram
    if stars:
        filters['stars'] = stars
    if stock:
        filters['stock'] = stock
    if min_price is not None:
        filters['min_price'] = min_price
    if max_price is not None:
        filters['max_price'] = max_price
    if category:
        filters['category'] = category

    filtered_products = service.get_products_by_attributes(**filters)
    return filtered_products

@router.get("/products/{product_id}", response_model=ProductBase)
async def get_product(product_id: int, service: ProductService = Depends(get_product_service)):
    """Get a specific product by ID."""
    product = service.get_product_by_id(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/products", response_model=ProductBase)
async def add_product(product: ProductBase, service: ProductService = Depends(get_product_service)):
    """Add a new product."""
    new_product = service.add_product(product)
    return new_product

@router.put("/products/{product_id}", response_model=ProductBase)
async def update_product(product_id: int, updated_product: ProductBase, service: ProductService = Depends(get_product_service)):
    """Update an existing product."""
    product = service.update_product(product_id, updated_product)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.delete("/products/{product_id}")
async def delete_product(product_id: int, service: ProductService = Depends(get_product_service)):
    """Delete a product by ID."""
    service.delete_product(product_id)
    return {"detail": "Product deleted successfully"}