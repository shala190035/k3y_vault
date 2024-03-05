from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
import shutil

# Stellen Sie sicher, dass FastAPI importiert wird, bevor Sie eine Instanz davon erstellen
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/products/")
def create_product(title: str, description: str, price: float, image: UploadFile = File(...), db: Session = Depends(get_db)):
    db_product = Product(title=title, description=description, price=price, image=image.filename)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    with open(f"images/{image.filename}", "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    return db_product

@app.get("/products/")
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = db.query(Product).offset(skip).limit(limit).all()
    return products
