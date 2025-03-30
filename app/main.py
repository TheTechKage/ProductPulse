
from fastapi import FastAPI, HTTPException
from database import Database
from dotenv import load_dotenv
from models.Base import base
from models import models
import os
from sqlalchemy import text


from schemas.product import Product
from schemas.category import Category
from utils import load_data
from typing import List, Dict

if __name__ == "__main__":
    try:
        load_dotenv()

        db=Database(
            os.getenv("SQLALCHEMY_DATABASE_URL"),
            os.getenv("DB_POOL_MIN_CONNECTION"),
            os.getenv("DB_POOL_MAX_CONNECTION"),
            # connection_params=[
            #     "echo": True,
                # "pool_timeout": 30,
                # "pool_recycle": 3600
            # ]
        ).db_engine

        # test connection
        if db:
            try:
                with db.connect() as connection:
                    query = text("SELECT version();")
                    result=connection.execute(query)
                    db_version=result.fetchone()
                    if(db_version):
                        print(f"Database version: {db_version[0]}")

                    baseop=base.metadata.create_all(db)
                    print("op --",baseop)
                    connection.commit()

            except Exception as e:
                print(f"Error executing query: {e}")

    except Exception as e:
        print(f"An error occurred in application: {e}")


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
