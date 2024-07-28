# func_py_find_word_occurrences.py
def func_py_find_word_occurrences(string, word):
    return string.lower().split().count(word.lower())

print(func_py_find_word_occurrences("This is a test. This is only a test.", "test"))
