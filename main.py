import pandas as pd
from datetime import datetime
from data import products, generate_random_time
from utils import sort_by_category_and_time, filter_by_category

def show_menu():
    print("\nProduct Management Menu")
    print("1. Show All Products")
    print("2. Add Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Sort by Category & Time")
    print("6. Filter by Category")
    print("0. Exit")

def show_all():
    df = pd.DataFrame(products)
    print(df)

def add_product():
    new_id = input("Enter ID: ")
    if any(p["id"].lower() == new_id.lower() for p in products):
        print("This ID already exists. Please enter a new ID (e.g., after P008).")
        return
    new_product = {
        "id": new_id,
        "category": input("Enter category: "),
        "price": float(input("Enter price: ")),
        "quantity": int(input("Enter quantity: ")),
        "rating": float(input("Enter rating (0–5): ")),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    products.append(new_product)
    print("Product added successfully.")

def update_product():
    print("\nCurrent Products:")
    for i, p in enumerate(products):
        print(f"{i}. {p['id']} - {p['category']} - {p['price']}")
    try:
        index = int(input("Enter index of product to update: "))
        if 0 <= index < len(products):
            new_id = input("New ID: ")
            new_category = input("New category: ")
            new_price = float(input("New price: "))
            new_quantity = int(input("New quantity: "))
            new_rating = float(input("New rating: "))
            products[index] = {
                "id": new_id,
                "category": new_category,
                "price": new_price,
                "quantity": new_quantity,
                "rating": new_rating,
                "time": generate_random_time()
            }
            print("Product updated.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter correct values.")

def delete_product():
    try:
        index = int(input("Enter index of product to delete: "))
        if 0 <= index < len(products):
            removed = products.pop(index)
            print(f"Deleted: {removed}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")

def sort_products():
    sorted_list = sort_by_category_and_time(products.copy())
    df = pd.DataFrame(sorted_list)
    print("Sorted Products by Category & Time:")
    print(df)

def filter_products():
    category = input("Enter category to filter: ")
    result = filter_by_category(products, category)
    if result:
        print(pd.DataFrame(result))
    else:
        print("No matching products found.")

while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        show_all()
    elif choice == "2":
        add_product()
    elif choice == "3":
        update_product()
    elif choice == "4":
        delete_product()
    elif choice == "5":
        sort_products()
    elif choice == "6":
        filter_products()
    elif choice == "0":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")
