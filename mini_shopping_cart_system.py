product = {
    "apple": 50,
    "banana": 20,
    "orange": 30,
    "grape": 40,
    "milk": 25
}

cart = {}

def show_products():
    print("\nAvailable Products:")
    for item, price in product.items():
        print(f"{item}: inr.{price}")

def add_to_cart():
    item = input("Enter the product name to add to cart: ").lower()
    
