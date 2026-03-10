def apply_discount(price, discount = 0.05):
    return price * (1 - discount)

def apply_tax(price, tax = 0.07):
    return price * (1 + tax)

def calculate_total(price, discount = 0.05, tax = 0.07):
    discounted = apply_discount(price, discount)
    return apply_tax(discounted, tax)

print(f"Total cost with default discount and tax: $ {calculate_total(120)}")
print(f"Total cost with custom discount and tax: $ {calculate_total(100, discount = 0.10, tax = 0.08)}")