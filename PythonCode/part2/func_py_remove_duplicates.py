# func_py_remove_duplicates.py

def func_py_remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def test_remove_duplicates():
    lists = [[1, 2, 2, 3, 4, 4, 5], ["a", "b", "b", "c", "c", "a"]]
    for lst in lists:
        print(f"List after removing duplicates: {func_py_remove_duplicates(lst)}")

if __name__ == "__main__":
    test_remove_duplicates()
