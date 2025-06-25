import csv

# Represent an inventory using a list of dictionaries.
inventory = [
    {"id": "P001", "name": "Laptop", "Price": 1200, "stock": 50},
    {"id": "P002", "name": "Mouse", "Price": 25, "stock": 150},
    {"id": "P003", "name": "Keyboard", "Price": 75, "stock": 70},
    {"id": "P004", "name": "Monitor", "Price": 300, "stock": 25},
    {"id": "P005", "name": "webcam", "Price": 50, "stock": 15},
]

print("----Inventory---")
for product in inventory:
    print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['Price']}, Stock: {product['stock']}")

def update_stock(product_id, quantity):
    found = False
    for product in inventory:
        if product["id"] == product_id:
            # Ensure stock does not go below zero after update
            if product["stock"] + quantity >= 0:
                product["stock"] += quantity
                print(f"Updated stock for {product['name']} (ID: {product['id']})")
            else:
                print(f"Error: Not enough stock for {product['name']}")
            found = True
            break
    if not found:
        print(f"Error: Product with ID '{product_id}' not found in inventory")

def get_low_stock_products(threshold):
    low_stock_products = []
    for product in inventory:
        if product["stock"] < threshold:
            low_stock_products.append(product)
    return low_stock_products

# --- Demonstrate the function ---
print("---Demonstrating stock updates---")
update_stock("P005", -10)
update_stock("P004", -30)  # This should trigger a low stock or error

# Write low stock products to CSV
csv_file_name = "low_stock_products.csv"
fieldnames = ["id", "name", "Price", "stock"]
print(f"Attempting to write low stock data to '{csv_file_name}'...")

low_stock_items = get_low_stock_products(1)

try:
    with open(csv_file_name, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(low_stock_items)
        print(f"Successfully wrote {len(low_stock_items)} low stock product(s) to '{csv_file_name}'.")
except IOError as e:
    print(f"Error: Could not write to file '{csv_file_name}'. {e}")