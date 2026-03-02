def calculate_total(price, tax_rate):
    """
    price: total price without tax
    tax_rate: tax percentage (e.g. 25 for 25%)
    returns: price including tax, rounded to 2 decimal places
    """
    total = price + price * (tax_rate / 100)
    return round(total, 2)