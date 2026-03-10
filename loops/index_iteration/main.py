prices = [29.99, 45.50, 12.75, 38.20]
for index in range(len(prices)):
    if index == 0:
        prices[index] *= 0.90
    elif index == 1:
        prices[index] *= 0.80
    elif index == 2:
        prices[index] *= 0.85
    else:
        prices[index] *= 0.95
    print(f"Updated price for item {index}: ${prices[index]:.2f}")