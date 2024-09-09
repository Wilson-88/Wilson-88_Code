# func_py_generate_list_of_even_numbers.py
def func_py_generate_list_of_even_numbers(n):
    return [x for x in range(n + 1) if x % 2 == 0]

print(func_py_generate_list_of_even_numbers(10))
