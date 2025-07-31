def group(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]

# Example
print(group([1, 2, 3, 4, 5, 6, 7], 3))
