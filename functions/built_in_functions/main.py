# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []
total_sales = 0

for product in products:
    price, quantity = products[product]
    price = float(price)
    quantity = int(quantity)
    total_sales = price * quantity
    total_sales_list.append(total_sales)
    print(f"total sales for {product}: ${total_sales}")

total_sum = sum(total_sales_list)
print("Total sum of all sales: $", total_sum)
min_sales = min(total_sales_list)
print("Minimum sales: $", min_sales)
max_sales = max(total_sales_list)
print("Maximum sales: $", max_sales)