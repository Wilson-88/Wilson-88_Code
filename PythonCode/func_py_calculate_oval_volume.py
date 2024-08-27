# func_py_calculate_oval_volume.py
import math

def func_py_calculate_oval_volume(radius1, radius2, height):
    return (4/3) * math.pi * radius1 * radius2 * height

print(func_py_calculate_oval_volume(3, 4, 5))
