# func_py_find_perfect_squares.py
def func_py_find_perfect_squares(limit):
    return [n for n in range(1, limit) if int(n**0.5)**2 == n]

print(func_py_find_perfect_squares(100))
