# func_py_count_occurrences.py

def func_py_count_occurrences(lst, element):
    return lst.count(element)

def test_count_occurrences():
    items = [1, 2, 3, 2, 4, 2]
    print(f"Occurrences of 2: {func_py_count_occurrences(items, 2)}")

if __name__ == "__main__":
    test_count_occurrences()
