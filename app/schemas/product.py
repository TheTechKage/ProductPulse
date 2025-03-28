from pydantic import BaseModel
from typing import List


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category: str
    inStock: bool
    colors: List[str]
