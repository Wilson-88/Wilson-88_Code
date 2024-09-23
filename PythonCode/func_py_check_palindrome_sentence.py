# func_py_check_palindrome_sentence.py
def func_py_check_palindrome_sentence(s):
    filtered_s = ''.join([char.lower() for char in s if char.isalnum()])
    return filtered_s == filtered_s[::-1]

print(func_py_check_palindrome_sentence("A man, a plan, a canal, Panama"))
