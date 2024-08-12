# func_py_convert_hexadecimal_to_decimal.py
def func_py_convert_hexadecimal_to_decimal(hex_str):
    try:
        return int(hex_str, 16)
    except ValueError:
        return None

print(func_py_convert_hexadecimal_to_decimal('1A'))
