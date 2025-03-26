# fun_py_reverse_each_word.py

def fun_py_reverse_each_word(s):
    return " ".join(word[::-1] for word in s.split())

def test_reverse_each_word():
    text = "Hello world"
    print(f"Reversed words: {fun_py_reverse_each_word(text)}")

if __name__ == "__main__":
    test_reverse_each_word()
