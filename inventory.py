inventory = [
    {"id": "P001", "name": "Laptop", "price": 1200, "stock": 50},
    {"id": "P002", "name": "Mouse", "price": 25, "stock": 150},
    {"id": "P003", "name": "Kryboard", "price": 75, "stock": 70},
    {"id": "P004", "name": "Monitor", "price": 300, "stock": 25},
    {"id": "P005", "name": "Webcam", "price": 50, "stock": 15}
]

print("--- Initial Inventory---")
for product in inventory:
    print(f"ID: {product['id']}, Name: {product['name']}, Stock: {product['stock']}" )
print("\n")


def update_stock(product_id, quantity):
    found = False
    for product in inventory:
        if product['id'] == product_id:
            if product['stock'] + quantity >= 0:
                product['stock'] += quantity
                print(f"Updated stock for {product['name']} ID: {product['id']}")
            else:
                print(f"Error: Not enough stock for {product['name']}")
            found = True
            break
    if not found:
        print(f"Eror: Product with ID '{product_id}' not found in the stock")


def get_low_stock_products(threshold):
    low_stock_products = []
    for product in inventory:
        if product['stock'] < threshold:
            low_stock_products.append(product['name'])
        print(low_stock_products)

#update_stock("P001", -100)
#get_low_stock_products(50)
