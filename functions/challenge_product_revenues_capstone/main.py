def calculate_revenue(prices, quantities_sold):
    revenue = []
    for item in range(len(prices)):
        revenue.append(prices[item] * quantities_sold[item])
    return revenue

def formatted_output(revenues):
    # revenues is already a sorted list of (product, revenue) tuples
    for item in revenues:
        print(f"{item[0]} has total revenue of ${item[1]}")

# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

# 1) Calculate revenue list
revenue = calculate_revenue(prices, quantities_sold)

# 2) Build and sort the top-level variable the tests expect
revenue_per_product = sorted(zip(products, revenue))

# 3) Print formatted output
formatted_output(revenue_per_product)