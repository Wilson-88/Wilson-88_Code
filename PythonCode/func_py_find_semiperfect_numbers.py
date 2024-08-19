# func_py_find_semiperfect_numbers.py
def func_py_find_semiperfect_numbers(limit):
    def divisors(num):
        return [i for i in range(1, num) if num % i == 0]

    def is_semiperfect(num):
        divisors_list = divisors(num)
        for i in range(1 << len(divisors_list)):
            subset_sum = sum(divisors_list[j] for j in range(len(divisors_list)) if i & (1 << j))
            if subset_sum == num:
                return True
        return False

    return [i for i in range(1, limit + 1) if is_semiperfect(i)]

print(func_py_find_semiperfect_numbers(100))
