from faker import Faker
from sqlalchemy import BigInteger, text
from sqlalchemy.orm import Session
from sqlalchemy.engine import Connection
from models import User, Product, Order
from database import SessionLocal, engine
import random
from openai import OpenAI
import os
import numpy as np
import json
from user_data import users
from product_data import products
client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
)


descriptions = {"Laptop": '''Discover the ultimate in portable computing with our sleek Laptop.
                 Featuring a powerful processor and expansive storage, it's your perfect companion for work and play,
                 whether you're at home or on the move.''',
                "Smartphone": '''Revolutionize your connectivity with our cutting-edge Smartphone.
                Boasting lightning-fast performance, a vibrant touchscreen, and stunning camera capabilities,
                    it keeps you connected and entertained wherever you go. ''',
                "Headphones": ''' Immerse yourself in superior sound quality with our premium Headphones. 
                Featuring advanced noise-canceling technology and luxurious comfort, 
                they're crafted for audiophiles and professionals seeking unparalleled audio experiences.''',
                "Keyboard": '''Elevate your typing experience with our ergonomic Keyboard. 
                Designed for precision and comfort, it offers customizable backlighting and responsive keys, 
                making it ideal for gamers and typists alike. ''',
                "Mouse": '''Navigate with precision using our high-performance Mouse. 
                Engineered for ergonomic comfort and precision accuracy, it's essential for enhancing productivity and gaming enjoyment with every click. ''',
                }

def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    embedding = client.embeddings.create(input=[text], model=model).data[0].embedding
    #print(str(embedding))
    return json.dumps(embedding)


def binary_to_vector(binary):
    return np.frombuffer(binary, dtype=np.float32)


def populate_with_fake_data_new(db: Session, connection: Connection):
    db.add_all(users)
    db.commit()

    product_ids = {}
    for product in products:
        embedding = product[5]  # This is a list of floats
        embedding_str = ','.join(map(str, embedding))
        result = connection.execute(
            text("""
                INSERT INTO products (product_name, price, quantity, product_description, image_path, description_embedding)
                VALUES (:product_name, :price, :quantity, :product_description, :image_path, JSON_ARRAY_PACK(:description_embedding))
            """),
            {
                "product_name": product[0],
                "price": product[1],
                "quantity": product[2],
                "product_description": product[3],
                "image_path": product[4],
                "description_embedding": product[5]  # Convert embedding to comma-separated string
            }
            

        )
        
    result = connection.execute(text("SELECT id, product_name FROM products")).fetchall()
    #print(result.fetchall())
    #print(result)
    for row in result:
       product_ids[row[1]] = row[0]
    print([row for row in result])
        
        
    connection.commit()

    orders = [
        Order(order_time="2022-06-15 12:30:00", quantity=1, product_id=product_ids['Laptop'], user_id=users[0].id),
        Order(order_time="2023-01-20 15:45:00", quantity=2, product_id=product_ids['Desk Lamp'], user_id=users[1].id),
        Order(order_time="2021-12-10 09:10:00", quantity=1, product_id=product_ids['Smartphone'], user_id=users[2].id),
        Order(order_time="2023-03-22 18:05:00", quantity=3, product_id=product_ids['Bracelet'], user_id=users[3].id),
        Order(order_time="2022-11-05 13:55:00", quantity=2, product_id=product_ids['Sunglasses'], user_id=users[4].id),
        Order(order_time="2023-05-12 11:20:00", quantity=1, product_id=product_ids['Backpack'], user_id=users[5].id),
        Order(order_time="2022-09-08 14:00:00", quantity=2, product_id=product_ids['Water Bottle'], user_id=users[6].id),
        Order(order_time="2023-04-18 16:30:00", quantity=1, product_id=product_ids['Blender'], user_id=users[7].id),
        Order(order_time="2022-08-25 10:15:00", quantity=3, product_id=product_ids['Sofa'], user_id=users[8].id),
        Order(order_time="2023-02-28 09:00:00", quantity=2, product_id=product_ids['Toaster'], user_id=users[9].id)
    ]
    db.add_all(orders)
    db.commit()

# Use this function
with SessionLocal() as db, engine.connect() as connection:
    populate_with_fake_data_new(db, connection)