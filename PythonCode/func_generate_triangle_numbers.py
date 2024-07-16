# func_generate_triangle_numbers.py
def func_generate_triangle_numbers(n):
    return [i * (i + 1) // 2 for i in range(1, n + 1)]

print(func_generate_triangle_numbers(10))
