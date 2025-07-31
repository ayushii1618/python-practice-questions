def triplet(n):
    result = set()
    for a in range(n):
        for b in range(a, n):
            c = a + b
            if c < n:
                result.add((a, b, c))
    return list(result)

# Example
print("Triplets:", triplet(10))
