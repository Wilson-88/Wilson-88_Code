# func_py_convert_decimal_to_hex.py
def func_py_convert_decimal_to_hex(n):
    try:
        return hex(n)[2:]
    except TypeError:
        return None

print(func_py_convert_decimal_to_hex(255))
print(func_py_convert_decimal_to_hex(1024))
