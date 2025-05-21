import pandas as pd
from datetime import datetime
from data import products, generate_random_time
from utils import sort_by_category, sort_by_time, filter_by_category

def is_valid_text(value):
    return value.isalpha()

def show_menu():
    print("\nProduct Management Menu")
    print("1. Show All Products")
    print("2. Add Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Sort by Category or Time")
    print("6. Filter by Category")
    print("0. Exit")

def show_all():
    df = pd.DataFrame(products)
    # Add "$" sign to price column just for display
    if "price" in df.columns:
        df["price"] = df["price"].apply(lambda x: f"${x:.2f}")
    print(df)


def add_product():
    print("\n[Add Product] — Type 'cancel' to cancel")

    while True:
        new_id = input("Enter New ID (P001): ").upper()
        if new_id == "CANCEL":
            return
        if not new_id.startswith("P"):
            print("ID must start with 'P'")
            continue
        if any(p["id"] == new_id for p in products):
            print("This ID already exists.")
            continue
        break

    while True:
        category = input("Enter category: ")
        if category.lower() == "cancel":
            return
        if not is_valid_text(category):
            print("Category must contain only letters.")
            continue
        break

    try:
        price = float(input("Enter price in $: "))
        quantity = int(input("Enter quantity: "))
        new_product = {
            "id": new_id,
            "category": category,
            "price": price,
            "quantity": quantity,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        products.append(new_product)
        print("✅ Product added.")
    except:
        print("❌ Invalid input.")

def update_product():
    print("\nAvailable Product IDs:")
    for p in products:
        print(f"- {p['id']}")

    target_id = input("Enter Product ID to update: ").upper()
    for i, p in enumerate(products):
        if p["id"] == target_id:
            while True:
                category = input("New category: ")
                if not is_valid_text(category):
                    print("Only letters allowed.")
                    continue
                break

            try:
                price = float(input("New price in $: "))
                quantity = int(input("New quantity: "))
                products[i] = {
                    "id": p["id"],
                    "category": category,
                    "price": price,
                    "quantity": quantity,
                    "time": generate_random_time()
                }
                print("✅ Product updated.")
                return
            except:
                print("❌ Invalid input.")
                return

    print("❌ Product ID not found.")

def delete_product():
    print("\nAvailable IDs:")
    for p in products:
        print(f"- {p['id']}")

    delete_id = input("Enter Product ID to delete: ").upper()
    for i, p in enumerate(products):
        if p["id"] == delete_id:
            products.pop(i)
            print("✅ Product deleted.")
            return
    print("❌ Product ID not found.")

def sort_products():
    print("Sort by:\n1. Category\n2. Time")
    choice = input("Enter choice: ")

    if choice == "1":
        sorted_data = sort_by_category(products.copy())
        print("\nSorted by Category:")
        print(pd.DataFrame(sorted_data))

        follow_up = input("\nAlso sort by Time?\n1. Yes\n2. No\nEnter: ")
        if follow_up == "1":
            sorted_data = sort_by_time(sorted_data)
            print("\nSorted by Category + Time:")
            print(pd.DataFrame(sorted_data))

    elif choice == "2":
        sorted_data = sort_by_time(products.copy())
        print("\nSorted by Time:")
        print(pd.DataFrame(sorted_data))

        follow_up = input("\nAlso sort by Category?\n1. Yes\n2. No\nEnter: ")
        if follow_up == "1":
            sorted_data = sort_by_category(sorted_data)
            print("\nSorted by Time + Category:")
            print(pd.DataFrame(sorted_data))

    else:
        print("Invalid choice.")


if __name__ == "__main__":
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
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")
