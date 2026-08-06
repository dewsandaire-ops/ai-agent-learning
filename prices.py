prices = {
    "Rice": 4500,
    "Beans": 3200,
    "Oil": 5000
}

item = input("Enter product: ")

if item in prices:
    print("Price:", prices[item])
else:
    print("Product not found.")