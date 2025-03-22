# fun_py_square_numbers.py

def fun_py_square_numbers(lst):
    return [x ** 2 for x in lst]

def test_square_numbers():
    numbers = [1, 2, 3, 4, 5]
    print(f"Squares: {fun_py_square_numbers(numbers)}")

if __name__ == "__main__":
    test_square_numbers()
