# func_py_convert_string_to_ascii.py
def func_py_convert_string_to_ascii(string):
    return [ord(char) for char in string]

print(func_py_convert_string_to_ascii("hello"))
