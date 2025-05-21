import random

def generate_random_time():
    year = 2025
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"

products = [
    {"id": "P001", "category": "Electronics", "name": "iPhone", "price": 999.0, "quantity": 10, "time": generate_random_time()},
    {"id": "P002", "category": "Furniture", "name": "Sofa", "price": 450.0, "quantity": 5, "time": generate_random_time()},
    {"id": "P003", "category": "Kitchen", "name": "Toaster", "price": 35.0, "quantity": 15, "time": generate_random_time()},
    {"id": "P004", "category": "Appliances", "name": "Washing Machine", "price": 700.0, "quantity": 3, "time": generate_random_time()},
    {"id": "P005", "category": "Clothing", "name": "Jacket", "price": 120.0, "quantity": 20, "time": generate_random_time()}
]
