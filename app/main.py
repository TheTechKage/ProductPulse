from fastapi import FastAPI

app = FastAPI()

@app.get("/api/products")
async def get_products():
    return {}

@app.get("/api/product/{id}")
async def get_product(id: int):
    return {}

@app.get("/api/categories")
async def get_categories():
    return {}

@app.get("/api/cart")
async def get_cart():
    return {}