from fastapi import FastAPI, HTTPException
from app.schemas.product import Product
from app.schemas.category import Category
from typing import List, Dict
import json

app = FastAPI()


@app.get("/api/products", response_model=List[Product])
async def get_products():
    with open("./data.json", "r") as f:
        data = json.load(f)
    return data.get("products")


@app.get("/api/product/{id}", response_model=Product)
async def get_product(id: int):
    with open("./data.json", "r") as f:
        data = json.load(f)

    products = data.get("products", [])
    for product in products:
        if product["id"] == id:
            return product

    raise HTTPException(status_code=404, detail=f"Product with id {id} not found")


@app.get("/api/categories", response_model=Dict[str, Category])
async def get_categories():
    with open("./data.json", "r") as f:
        data = json.load(f)
    return data.get("categories", {})


@app.get("/api/cart", response_model=Dict)
async def get_cart():
    return {}
