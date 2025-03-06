# func_py_extract_urls_from_text.py
import re

def func_py_extract_urls_from_text(text):
    return re.findall(r'https?://\S+', text)

text = "Check https://example.com and http://test.com"
print(func_py_extract_urls_from_text(text))
