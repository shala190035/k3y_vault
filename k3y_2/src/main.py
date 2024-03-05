from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from model import Product
from database import SessionLocal  # Passen Sie den Importpfad entsprechend Ihrer Dateistruktur an
import shutil

# Stellen Sie sicher, dass FastAPI importiert wird, bevor Sie eine Instanz davon erstellen
app = FastAPI()

# Liste der erlaubten Ursprünge (hier fügen Sie die URL Ihres Frontends ein)
origins = [
    "http://localhost:5173",  # Vue-App
    "http://127.0.0.1:5173"   # Falls Sie auch 127.0.0.1 verwenden
]

# CORS Middleware Konfiguration
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Alle Ursprünge aus der Liste erlauben
    allow_credentials=True,
    allow_methods=["*"],  # Erlaube alle Methoden
    allow_headers=["*"],  # Erlaube alle Header
)

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
