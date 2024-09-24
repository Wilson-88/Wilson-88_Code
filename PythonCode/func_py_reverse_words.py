# func_py_reverse_words.py
def func_py_reverse_words(s):
    return ' '.join(word[::-1] for word in s.split())

print(func_py_reverse_words("hello world"))
