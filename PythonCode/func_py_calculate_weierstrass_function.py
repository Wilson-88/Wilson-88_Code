# func_py_calculate_weierstrass_function.py
import numpy as np
import matplotlib.pyplot as plt

def func_py_calculate_weierstrass_function(a, b, x, n):
    result = sum(a**i * np.cos(b**i * np.pi * x) for i in range(n))
    return result

x = np.linspace(-2, 2, 1000)
y = [func_py_calculate_weierstrass_function(0.5, 3, xi, 20) for xi in x]
plt.plot(x, y)
plt.title("Weierstrass Function")
plt.show()
