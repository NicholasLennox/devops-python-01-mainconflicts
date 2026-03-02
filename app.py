from utils.pricing import calculate_total    

total_price = 100
tax = 25
result = calculate_total(total_price, tax)
print(f"Total cost: {result}")