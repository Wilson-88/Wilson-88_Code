# func_py_generate_lucas_numbers.py
def func_py_generate_lucas_numbers(limit):
    lucas_numbers = [2, 1]
    for i in range(2, limit):
        lucas_numbers.append(lucas_numbers[-1] + lucas_numbers[-2])
    return lucas_numbers

print(func_py_generate_lucas_numbers(10))
