# func_py_create_histogram.py
def func_py_create_histogram(lst):
    histogram = {}
    for num in lst:
        if num in histogram:
            histogram[num] += 1
        else:
            histogram[num] = 1
    return histogram
