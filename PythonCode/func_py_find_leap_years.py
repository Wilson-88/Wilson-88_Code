# func_py_find_leap_years.py
def func_py_find_leap_years(start_year, end_year):
    return [year for year in range(start_year, end_year + 1) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]

print(func_py_find_leap_years(2000, 2024))
