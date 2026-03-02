def calculate_total(price, tax_rate):
    """
    price: total price withot tax
    tax_rate: tax percentage as a number (e.g. 25 for 25%)
    returns: price including tax
    """
    return price + price*(tax_rate/100)