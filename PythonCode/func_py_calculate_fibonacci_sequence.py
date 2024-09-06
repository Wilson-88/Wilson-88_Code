# func_py_calculate_fibonacci_sequence.py
def func_py_calculate_fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

print(func_py_calculate_fibonacci_sequence(10))
