def my_filter(func, lst):
    return [x for x in lst if func(x)]

# Example
print(my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
