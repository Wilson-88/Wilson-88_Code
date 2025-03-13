# func_py_list_intersection.py
def func_py_list_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

print(func_py_list_intersection([1, 2, 3, 4], [3, 4, 5, 6]))
