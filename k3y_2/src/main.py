from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Base, engine, Product, SessionLocal
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # The Vue.js app's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ProductBase(BaseModel):
    name: str
    price: float
    description: str

@app.post("/products/", response_model=ProductBase)
def create_product(product: ProductBase, db: Session = Depends(get_db)):
    db_product = Product(name=product.name, price=product.price, description=product.description)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get("/products/", response_model=List[ProductBase])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = db.query(Product).offset(skip).limit(limit).all()
    return products
