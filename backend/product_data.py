from openai import OpenAI
import os
import json

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
) 

def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    embedding = client.embeddings.create(input=[text], model=model).data[0].embedding
    return json.dumps(embedding)

descriptions = {
    "Laptop": "A high-performance laptop suitable for all your computing needs. It features a sleek design and powerful hardware, making it perfect for both work and entertainment.",
    "Tablet": "A versatile tablet with a vibrant display and long battery life. Ideal for browsing, reading, and on-the-go productivity.",
    "Smartphone": "A cutting-edge smartphone with a stunning display and advanced camera capabilities. Stay connected with lightning-fast performance and sleek design.",
    "Smartwatch": "A stylish smartwatch that keeps you connected and tracks your fitness. Features include heart rate monitoring, notifications, and customizable watch faces.",
    "Headphones": "High-quality headphones delivering immersive sound. Comfortable and perfect for music, calls, and gaming.",
    "Earbuds": "Compact and convenient earbuds with excellent sound quality. Ideal for listening to music and taking calls on the go.",
    "Keyboard": "A durable keyboard with responsive keys and customizable backlighting. Perfect for typing and gaming.",
    "Mouse": "A precise and ergonomic mouse for all your computing needs. Features customizable buttons and smooth tracking.",
    "Book": "A captivating book that will transport you to another world. Perfect for readers of all ages who love a good story.",
    "Magazine": "A glossy magazine filled with the latest trends and articles. Great for keeping up with current events and entertainment.",
    "Desk Lamp": "A stylish desk lamp providing bright and adjustable lighting. Ideal for reading, studying, and working.",
    "Floor Lamp": "A modern floor lamp with a sleek design. Provides ample lighting for any room in your home.",
    "Blender": "A powerful blender perfect for smoothies, soups, and more. Easy to use and clean, with multiple speed settings.",
    "Toaster": "A reliable toaster with adjustable browning settings. Perfect for making crisp and delicious toast every time.",
    "Sofa": "A comfortable and stylish sofa for your living room. Offers ample seating and complements any home decor.",
    "Armchair": "A cozy armchair perfect for relaxing. Features soft cushions and a sturdy frame.",
    "Coffee Maker": "A convenient coffee maker for a perfect cup every morning. Features programmable settings and a sleek design.",
    "Kettle": "A fast-boiling kettle with a modern design. Perfect for making tea, coffee, and other hot beverages.",
    "Running Shoes": "Lightweight and comfortable running shoes designed for performance. Ideal for jogging, running, and other athletic activities.",
    "Hiking Boots": "Durable hiking boots with excellent grip and support. Perfect for outdoor adventures and rough terrains.",
    "Bicycle": "A sturdy and reliable bicycle for commuting and leisure rides. Features a comfortable seat and smooth gears.",
    "Scooter": "A fun and easy-to-ride scooter for kids and adults. Great for short commutes and recreational use.",
    "Watch": "A classic watch with a timeless design. Features a durable strap and precise timekeeping.",
    "Bracelet": "A stylish bracelet that adds a touch of elegance to any outfit. Made with high-quality materials.",
    "Sunglasses": "Chic sunglasses that offer UV protection and style. Perfect for sunny days and outdoor activities.",
    "Hat": "A fashionable hat that provides shade and complements any outfit. Ideal for both casual and formal occasions.",
    "Backpack": "A spacious and durable backpack for school, work, or travel. Features multiple compartments and a comfortable design.",
    "Suitcase": "A lightweight and sturdy suitcase with ample storage. Perfect for all your travel needs, with smooth-rolling wheels.",
    "Water Bottle": "A reusable water bottle that keeps your drinks cold or hot for hours. Eco-friendly and perfect for staying hydrated on the go.",
    "Thermos": "An insulated thermos that maintains the temperature of your beverages. Ideal for carrying coffee, tea, or soup."
}

products = [
    ("Laptop", 799.99, 50, descriptions["Laptop"], "/images/laptop.jpg", get_embedding(descriptions["Laptop"])),
    ("Tablet", 399.99, 60, descriptions["Tablet"], "/images/tablet.jpg", get_embedding(descriptions["Tablet"])),
    ("Smartphone", 499.99, 100, descriptions["Smartphone"], "/images/smartphone.jpg", get_embedding(descriptions["Smartphone"])),
    ("Smartwatch", 199.99, 120, descriptions["Smartwatch"], "/images/smartwatch.jpg", get_embedding(descriptions["Smartwatch"])),
    ("Headphones", 199.99, 200, descriptions["Headphones"], "/images/headphones.jpg", get_embedding(descriptions["Headphones"])),
    ("Earbuds", 149.99, 250, descriptions["Earbuds"], "/images/earbuds.jpg", get_embedding(descriptions["Earbuds"])),
    ("Keyboard", 99.99, 150, descriptions["Keyboard"], "/images/keyboard.jpg", get_embedding(descriptions["Keyboard"])),
    ("Mouse", 49.99, 300, descriptions["Mouse"], "/images/mouse.jpg", get_embedding(descriptions["Mouse"])),
    ("Book", 14.99, 500, descriptions["Book"], "/images/book.jpg", get_embedding(descriptions["Book"])),
    ("Magazine", 5.99, 600, descriptions["Magazine"], "/images/magazine.jpg", get_embedding(descriptions["Magazine"])),
    ("Desk Lamp", 29.99, 150, descriptions["Desk Lamp"], "/images/desklamp.jpg", get_embedding(descriptions["Desk Lamp"])),
    ("Floor Lamp", 69.99, 80, descriptions["Floor Lamp"], "/images/floorlamp.jpg", get_embedding(descriptions["Floor Lamp"])),
    ("Blender", 89.99, 80, descriptions["Blender"], "/images/blender.jpg", get_embedding(descriptions["Blender"])),
    ("Toaster", 39.99, 100, descriptions["Toaster"], "/images/toaster.jpg", get_embedding(descriptions["Toaster"])),
    ("Sofa", 399.99, 30, descriptions["Sofa"], "/images/sofa.jpg", get_embedding(descriptions["Sofa"])),
    ("Armchair", 199.99, 40, descriptions["Armchair"], "/images/armchair.jpg", get_embedding(descriptions["Armchair"])),
    ("Coffee Maker", 59.99, 120, descriptions["Coffee Maker"], "/images/coffeemaker.jpg", get_embedding(descriptions["Coffee Maker"])),
    ("Kettle", 29.99, 150, descriptions["Kettle"], "/images/kettle.jpg", get_embedding(descriptions["Kettle"])),
    ("Running Shoes", 69.99, 200, descriptions["Running Shoes"], "/images/runningshoes.jpg", get_embedding(descriptions["Running Shoes"])),
    ("Hiking Boots", 89.99, 100, descriptions["Hiking Boots"], "/images/hikingboots.jpg", get_embedding(descriptions["Hiking Boots"])),
    ("Bicycle", 299.99, 40, descriptions["Bicycle"], "/images/bicycle.jpg", get_embedding(descriptions["Bicycle"])),
    ("Scooter", 149.99, 50, descriptions["Scooter"], "/images/scooter.jpg", get_embedding(descriptions["Scooter"])),
    ("Watch", 149.99, 100, descriptions["Watch"], "/images/watch.jpg", get_embedding(descriptions["Watch"])),
    ("Bracelet", 49.99, 200, descriptions["Bracelet"], "/images/bracelet.jpg", get_embedding(descriptions["Bracelet"])),
    ("Sunglasses", 79.99, 150, descriptions["Sunglasses"], "/images/sunglasses.jpg", get_embedding(descriptions["Sunglasses"])),
    ("Hat", 29.99, 200, descriptions["Hat"], "/images/hat.jpg", get_embedding(descriptions["Hat"])),
    ("Backpack", 39.99, 200, descriptions["Backpack"], "/images/backpack.jpg", get_embedding(descriptions["Backpack"])),
    ("Suitcase", 89.99, 150, descriptions["Suitcase"], "/images/suitcase.jpg", get_embedding(descriptions["Suitcase"])),
    ("Water Bottle", 14.99, 300, descriptions["Water Bottle"], "/images/waterbottle.jpg", get_embedding(descriptions["Water Bottle"])),
    ("Thermos", 24.99, 200, descriptions["Thermos"], "/images/thermos.jpg", get_embedding(descriptions["Thermos"]))
]