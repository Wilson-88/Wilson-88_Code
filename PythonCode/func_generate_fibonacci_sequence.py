# func_generate_fibonacci_sequence.py
def func_generate_fibonacci_sequence(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

print(func_generate_fibonacci_sequence(10))
