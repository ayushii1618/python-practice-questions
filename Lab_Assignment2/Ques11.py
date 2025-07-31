def my_map(func, lst):
    return [func(x) for x in lst]

# Example
print(my_map(lambda x: x*2, [1, 2, 3, 4]))
