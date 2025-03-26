from fastapi import FastAPI
from database.db import DatabasePool
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    try:
        load_dotenv()
        connection_pool=DatabasePool(
            os.getenv("DB_POOL_MIN_CONNECTION"),
            os.getenv("DB_POOL_MAX_CONNECTION"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_DB_PORT"),
            database=os.getenv("POSTGRES_DB")
        )

        connection =connection_pool.get_connection()

    except Exception as e:
        print(f"An error occurred: {e}")


# app = FastAPI()

# @app.get("/api/products")
# async def get_products():
#     return {}

# @app.get("/api/product/{id}")
# async def get_product(id: int):
#     return {}

# @app.get("/api/categories")
# async def get_categories():
#     return {}

# @app.get("/api/cart")
# async def get_cart():
#     return {}