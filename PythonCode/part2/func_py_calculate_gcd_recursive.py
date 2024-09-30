# func_py_calculate_gcd_recursive.py
def func_py_calculate_gcd_recursive(a, b):
    if b == 0:
        return a
    return func_py_calculate_gcd_recursive(b, a % b)
