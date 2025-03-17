# func_py_caesar_cipher.py

def func_py_caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def test_caesar_cipher():
    print(f"Encrypted: {func_py_caesar_cipher('Hello, World!', 3)}")

if __name__ == "__main__":
    test_caesar_cipher()
