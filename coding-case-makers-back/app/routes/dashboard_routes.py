# app/routes/dashboard.py

from fastapi import APIRouter, Depends
from app.services.product_service import ProductService
from app.dependencies import get_product_service

router = APIRouter()


@router.get("/dashboard")
async def dashboard(service: ProductService = Depends(get_product_service)):
    """
    Dashboard endpoint accessible to all users.
    Returns the total product count, stock metrics,
    total products by brand, and total stock by brand.
    """
    total_products = service.get_product_count()
    total_stock, out_of_stock_count = service.get_stock_info()
    products_by_brand = service.get_products_by_brand()

    return {
        "total_products": total_products,
        "total_stock": total_stock,
        "out_of_stock_count": out_of_stock_count,
        "products_by_brand": products_by_brand,
    }