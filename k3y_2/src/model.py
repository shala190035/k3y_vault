from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func

# Database URL, adjust as needed for your setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Session local for database connection
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    image = Column(String)  # Stores the path to the image file

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    address = Column(String)
    payment_method = Column(String)
    total = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    order_items = relationship("OrderItem", back_populates="order")  # Relationship to order items

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    price = Column(Float)  # Could be redundant, but useful if prices change over time and you want historical accuracy
    order = relationship("Order", back_populates="order_items")  # Link back to the order
    product = relationship("Product")  # Link to the product

# Creates all tables in the database (this should be done once)
Base.metadata.create_all(bind=engine)
