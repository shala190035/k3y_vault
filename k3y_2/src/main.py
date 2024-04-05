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
        address = order_details['order']['address']
        payment_method = order_details['order']['paymentMethod']
        items = order_details['order']['items']
        total = order_details['order']['total']

        # Create order instance
        order = Order(email=email, address=address, payment_method=payment_method, total=total)
        db.add(order)
        db.commit()
        db.refresh(order)

        # Create order item instances
        for item in items:
            order_item = OrderItem(order_id=order.id, product_id=item['id'], quantity=item['quantity'], price=item['price'])
            db.add(order_item)
        
        db.commit()
        email_content = f"""
        <html>
            <head></head>
            <body>
                <h1>Thank you for your order #{order.id}!</h1>
                <p>Your order details are as follows:</p>
                <table>
                    <tr>
                        <th>Item</th>
                        <th>Quantity</th>
                        <th>Price</th>
                    </tr>
                    {''.join([f"<tr><td>{item['title']}</td><td> X {item['quantity']}</td><td>{item['price']} €</td></tr>" for item in items])}
                </table>
                <p>Total: <strong>{total} €</strong></p>
                <p>Delivery Address: {address}</p>
                <p>Payment Method: {payment_method}</p>
                <p>We are processing your order and will send you a confirmation once it's shipped.</p>
            </body>
        </html>
        """
        message = Mail(
            from_email='wadu0185@gmail.com',  # Ensure this email is verified in SendGrid.
            to_emails=email,
            subject=f'Order Confirmation #{order.id}',
            html_content=email_content
        )
        sendgrid_api_key = os.getenv('SENDGRID_API_KEY')
        if not sendgrid_api_key:
            raise Exception("SendGrid API key not found.")
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)
        print(f"Email sent. Status Code: {response.status_code}, Body: {response.body}")
        return {"message": "Order confirmation email sent successfully.", "orderId": order.id}
    except Exception as e:
        print(f"Error sending email: {e}")  # Log the full error
        raise HTTPException(status_code=500, detail=str(e))
