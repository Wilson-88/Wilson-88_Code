# fun_py_find_median.py

def fun_py_find_median(lst):
    sorted_lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    return (sorted_lst[mid] if n % 2 else (sorted_lst[mid - 1] + sorted_lst[mid]) / 2)

def test_find_median():
    numbers = [10, 20, 30, 40, 50]
    print(f"Median of list: {fun_py_find_median(numbers)}")

if __name__ == "__main__":
    test_find_median()
