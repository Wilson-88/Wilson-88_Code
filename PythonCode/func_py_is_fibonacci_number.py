# func_py_is_fibonacci_number.py
def func_py_is_fibonacci_number(n):
    def is_perfect_square(x):
        s = int(x**0.5)
        return s*s == x

    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

print(func_py_is_fibonacci_number(21))
