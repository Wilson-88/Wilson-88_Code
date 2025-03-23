# fun_py_count_occurrences.py

from collections import Counter

def fun_py_count_occurrences(lst):
    return dict(Counter(lst))

def test_count_occurrences():
    numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]
    print(f"Occurrences: {fun_py_count_occurrences(numbers)}")

if __name__ == "__main__":
    test_count_occurrences()
