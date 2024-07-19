# func_find_combinations_of_list.py
from itertools import combinations

def func_find_combinations_of_list(lst, r):
    return list(combinations(lst, r))

print(func_find_combinations_of_list([1, 2, 3, 4], 2))
