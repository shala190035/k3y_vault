from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, Body
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from model import Product, Order, OrderItem
from database import SessionLocal
import shutil
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv  # Import dotenv
import os
import logging

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

app.mount("/images", StaticFiles(directory="images"), name="images")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/products/")
async def create_product(title: str, description: str, price: float, image: UploadFile = File(...), db: Session = Depends(get_db)):
    image_path = f"images/{image.filename}"
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    
    db_product = Product(title=title, description=description, price=price, image=image_path)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get("/products/")
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = db.query(Product).offset(skip).limit(limit).all()
    return products

@app.post("/submit-order")
async def submit_order(order_details: dict = Body(...), db: Session = Depends(get_db)):
    try:
        email = order_details['email']
        order = order_details['order']
        # Path or URL to your logo
        logo_url = "http://localhost:5173/src/assets/logo_noname.png"  # Change to the actual path of your logo
        company_name = "K3Y"
        
        # Create email content with logo and company name
        email_content = f"""
        <html>
            <head></head>
            <body>
                <div style="text-align: center;">
                    <img src="{logo_url}" alt="Company Logo" style="width: 150px;"><br>
                    <h2>{company_name}</h2>
                </div>
                <h1>Thank you for your order!</h1>
                <p>The details of your order are as follows:</p>
                <table>
                    <tr>
                        <th>Item</th>
                        <th>Quantity</th>
                        <th>Price</th>
                    </tr>
                    {''.join([f"<tr><td>{item['title']}</td><td>{item['quantity']}</td><td>{item['price']} €</td></tr>" for item in order['items']])}
                </table>
                <p>Total: <strong>{order['total']} €</strong></p>
                <p>Delivery Address: {order['address']}</p>
                <p>Payment Method: {order['paymentMethod']}</p>
                <p>We are processing your order and will send you a confirmation once it's shipped.</p>
            </body>
        </html>
        """
        message = Mail(
            from_email='wadu0185@gmail.com',  # Ensure this email is verified with SendGrid.
            to_emails=email,
            subject='Order Confirmation',
            html_content=email_content
        )
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)
        return {"message": "Order confirmation email sent successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/track-order")
async def track_order(order_id: int = Body(...), address: str = Body(...), db: Session = Depends(get_db)):
    logging.info(f"Tracking order: ID={order_id}, Address='{address}'")
    order = db.query(Order).filter(Order.id == order_id, Order.address == address).first()
    if not order:
        logging.warn(f"Order not found: ID={order_id}, Address='{address}'")
        raise HTTPException(status_code=404, detail="Order not found or address does not match")
    order_details = format_order_details(order)
    return order_details

@app.post("/track-order/")
async def track_order(order_id: int, address: str, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id, Order.address == address).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found or address does not match")
    order_details = format_order_details(order)
    return {"order_details": order_details}

def format_order_details(order):
    items_details = [{"title": item.product.title, "quantity": item.quantity, "price": item.price} for item in order.order_items]
    return {
        "id": order.id,
        "email": order.email,
        "address": order.address,
        "payment_method": order.payment_method,
        "total": order.total,
        "status": order.status,  # Include status in the response
        "items": items_details,
        "created_at": order.created_at.isoformat(),
    }
