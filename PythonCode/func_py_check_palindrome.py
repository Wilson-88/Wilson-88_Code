# func_py_check_palindrome.py
def func_py_check_palindrome(string):
    return string == string[::-1]

print(func_py_check_palindrome("radar"))
print(func_py_check_palindrome("hello"))
