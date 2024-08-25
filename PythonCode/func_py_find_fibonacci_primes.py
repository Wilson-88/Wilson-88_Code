# func_py_find_fibonacci_primes.py
def func_py_find_fibonacci_primes(limit):
    def is_prime(num):
        return all(num % i != 0 for i in range(2, int(num**0.5) + 1))
    
    fibs = [0, 1]
    while len(fibs) < limit:
        fibs.append(fibs[-1] + fibs[-2])
    
    return [f for f in fibs if is_prime(f) and f > 1]

print(func_py_find_fibonacci_primes(10))
