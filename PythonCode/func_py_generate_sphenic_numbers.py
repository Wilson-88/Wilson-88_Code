# func_py_generate_sphenic_numbers.py
def func_py_generate_sphenic_numbers(limit):
    def is_prime(num):
        return all(num % i != 0 for i in range(2, int(num**0.5) + 1))
    
    sphenic_numbers = []
    for n in range(2, limit):
        prime_factors = [i for i in range(2, n) if n % i == 0 and is_prime(i)]
        if len(prime_factors) == 3:
            sphenic_numbers.append(n)
    
    return sphenic_numbers

print(func_py_generate_sphenic_numbers(100))
