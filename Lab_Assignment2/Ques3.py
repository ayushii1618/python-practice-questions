def duplicate(lst):
    seen = set()
    duplicates = set()
    for num in lst:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

# Example
nums = [1, 2, 3, 2, 4, 5, 3, 6, 1, 7]
print("Duplicates:", duplicate(nums))
