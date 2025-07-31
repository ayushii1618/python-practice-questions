import string

def mutate(word):
    letters = string.ascii_lowercase
    mutations = set()

    # Insert
    for i in range(len(word) + 1):
        for c in letters:
            mutations.add(word[:i] + c + word[i:])

    # Delete
    for i in range(len(word)):
        mutations.add(word[:i] + word[i+1:])

    # Replace
    for i in range(len(word)):
        for c in letters:
            if word[i] != c:
                mutations.add(word[:i] + c + word[i+1:])

    # Swap
    for i in range(len(word) - 1):
        swapped = list(word)
        swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]
        mutations.add("".join(swapped))

    return mutations

def nearly_equal(a, b):
    return a in mutate(b)

# ✅ Examples
print(nearly_equal("cats", "cat"))    # True (insert)
print(nearly_equal("cat", "cats"))    # True (delete)
print(nearly_equal("cut", "cat"))     # True (replace)
print(nearly_equal("act", "cat"))     # True (swap)
print(nearly_equal("dog", "cat"))     # False
