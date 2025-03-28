from fastapi import FastAPI, HTTPException
from app.schemas.product import Product
from app.schemas.category import Category
from app.utils import load_data
from typing import List, Dict

app = FastAPI()


@app.get("/api/products", response_model=List[Product])
async def get_products():
    data = load_data()
    return data.get("products")


@app.get("/api/product/{id}", response_model=Product)
async def get_product(id: int):
    data = load_data()
    products = data.get("products", [])
    for product in products:
        if product["id"] == id:
            return product

    raise HTTPException(status_code=404, detail=f"Product with id {id} not found")


@app.get("/api/products/search", response_model=List[Product])
async def search_products(query: str):
    data = load_data()
    products = data.get("products", [])
    return [product for product in products if query.lower() in product["name"].lower()]


@app.get("/api/categories", response_model=Dict[str, Category])
async def get_categories():
    data = load_data()
    return data.get("categories", {})


@app.get("/api/cart", response_model=Dict)
async def get_cart():
    return {}
