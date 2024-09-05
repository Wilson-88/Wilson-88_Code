# func_py_calculate_greatest_common_divisor.py
def func_py_calculate_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

print(func_py_calculate_greatest_common_divisor(48, 18))
