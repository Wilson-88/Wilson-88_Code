# func_py_check_armstrong_number.py
def func_py_check_armstrong_number(num):
    digits = list(map(int, str(num)))
    return num == sum([digit ** len(digits) for digit in digits])

print(func_py_check_armstrong_number(153))
