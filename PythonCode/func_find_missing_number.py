# func_find_missing_number.py
def func_find_missing_number(lst):
    n = len(lst) + 1
    total_sum = n * (n + 1) // 2
    return total_sum - sum(lst)

print(func_find_missing_number([1, 2, 4, 5, 6]))
