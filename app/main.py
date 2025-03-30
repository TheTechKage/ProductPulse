from fastapi import FastAPI
from database import Database
from dotenv import load_dotenv
from models.Base import base
from models import models
import os
from sqlalchemy import text

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