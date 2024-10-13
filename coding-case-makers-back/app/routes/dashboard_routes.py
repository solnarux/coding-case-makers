# app/routes/dashboard.py

from fastapi import APIRouter, Depends
from app.services.product_service import ProductService
from app.dependencies import get_product_service

router = APIRouter()


@router.get("/dashboard")
async def dashboard(service: ProductService = Depends(get_product_service)):
    """
    Dashboard endpoint accessible to all users.
    Returns the total product count and stock metrics.
    """
    total_products = service.get_product_count()
    total_stock, out_of_stock_count = service.get_stock_info()

    return {
        "total_products": total_products,
        "total_stock": total_stock,
        "out_of_stock_count": out_of_stock_count,
    }