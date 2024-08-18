# func_py_generate_balanced_numbers.py
def func_py_generate_balanced_numbers(limit):
    def is_balanced(num):
        digits = [int(digit) for digit in str(num)]
        midpoint = len(digits) // 2
        return sum(digits[:midpoint]) == sum(digits[-midpoint:])
    
    return [i for i in range(1, limit + 1) if is_balanced(i)]

print(func_py_generate_balanced_numbers(1000))
