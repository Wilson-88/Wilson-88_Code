# func_py_mode.py

from collections import Counter

def func_py_mode(lst):
    count = Counter(lst)
    return max(count, key=count.get)

def test_mode():
    numbers = [1, 2, 2, 3, 4, 4, 4, 5]
    print(f"Mode: {func_py_mode(numbers)}")

if __name__ == "__main__":
    test_mode()
