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
    {"id": "P001", "category": "Electronics", "price": 100.0, "quantity": 10, "rating": 4.5, "time": generate_random_time()},
    {"id": "P002", "category": "Furniture", "price": 250.0, "quantity": 5, "rating": 4.2, "time": generate_random_time()},
    {"id": "P003", "category": "Kitchen", "price": 40.0, "quantity": 20, "rating": 4.0, "time": generate_random_time()},
    {"id": "P004", "category": "Electronics", "price": 300.0, "quantity": 8, "rating": 4.8, "time": generate_random_time()},
    {"id": "P005", "category": "Appliances", "price": 150.0, "quantity": 12, "rating": 4.1, "time": generate_random_time()}
]
