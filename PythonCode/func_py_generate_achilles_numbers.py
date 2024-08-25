# func_py_generate_achilles_numbers.py
def func_py_generate_achilles_numbers(limit):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def prime_factors(num):
        factors = []
        divisor = 2
        while num > 1:
            while num % divisor == 0:
                factors.append(divisor)
                num //= divisor
            divisor += 1
        return factors
    
    achilles_numbers = []
    for n in range(2, limit):
        factors = prime_factors(n)
        if len(set(factors)) > 1 and all(gcd(f, n//f) == 1 for f in factors):
            achilles_numbers.append(n)
    return achilles_numbers

print(func_py_generate_achilles_numbers(100))
