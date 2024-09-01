# func_py_generate_harshad_numbers.py
def func_py_generate_harshad_numbers(limit):
    harshad_numbers = [n for n in range(1, limit + 1) if n % sum(map(int, str(n))) == 0]
    return harshad_numbers

print(func_py_generate_harshad_numbers(100))
