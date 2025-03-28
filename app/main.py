from fastapi import FastAPI, HTTPException
import json

app = FastAPI()


@app.get("/api/products")
async def get_products():
    with open("./data.json", "r") as f:
        data = json.load(f)
    return data.get("products")


@app.get("/api/product/{id}")
async def get_product(id: int):
    with open("./data.json", "r") as f:
        data = json.load(f)

    products = data.get("products", [])
    for product in products:
        if product["id"] == id:
            return product

    raise HTTPException(status_code=404, detail=f"Product with id {id} not found")


@app.get("/api/categories")
async def get_categories():
    with open("./data.json", "r") as f:
        data = json.load(f)
    return data.get("categories", {})


@app.get("/api/cart")
async def get_cart():
    return {}
