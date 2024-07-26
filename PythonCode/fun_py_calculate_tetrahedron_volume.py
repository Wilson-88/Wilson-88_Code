# fun_py_calculate_tetrahedron_volume.py
import math

def fun_py_calculate_tetrahedron_volume(edge):
    return (edge ** 3) / (6 * math.sqrt(2))

print(fun_py_calculate_tetrahedron_volume(3))
