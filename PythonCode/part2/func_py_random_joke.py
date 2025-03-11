# func_py_random_joke.py
import requests

def func_py_random_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        joke = response.json()
        return f"{joke['setup']} - {joke['punchline']}"
    return "Failed to fetch joke"

print(func_py_random_joke())
