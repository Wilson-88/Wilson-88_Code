# func_py_convert_int_to_binary_string.py
def func_py_convert_int_to_binary_string(n):
    try:
        return format(n, 'b')
    except TypeError:
        return None

print(func_py_convert_int_to_binary_string(10))
print(func_py_convert_int_to_binary_string(255))
