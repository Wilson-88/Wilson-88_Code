# func_py_calculate_ferris_wheel_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_ferris_wheel_curve(r, points):
    t = np.linspace(0, 2 * np.pi, points)
    x = r * np.cos(t)
    y = r * np.sin(t)
    plt.plot(x, y)
    plt.title("Ferris Wheel Curve")
    plt.show()

func_py_calculate_ferris_wheel_curve(5, 1000)
