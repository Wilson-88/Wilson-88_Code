# func_py_find_centered_square_numbers.py
def func_py_find_centered_square_numbers(limit):
    return [n**2 + (n-1)**2 for n in range(1, limit + 1)]

print(func_py_find_centered_square_numbers(10))
