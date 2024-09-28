# func_py_calculate_total_price.py
def func_py_calculate_total_price(price, tax_rate):
    return price + (price * tax_rate / 100)

print(func_py_calculate_total_price(100, 7))
