import string

def mutate(word):
    letters = string.ascii_lowercase
    mutations = set()

    # Insert
    for i in range(len(word)+1):
        for c in letters:
            mutations.add(word[:i] + c + word[i:])

    # Delete
    for i in range(len(word)):
        mutations.add(word[:i] + word[i+1:])

    # Replace
    for i in range(len(word)):
        for c in letters:
            mutations.add(word[:i] + c + word[i+1:])

    # Swap
    for i in range(len(word)-1):
        swapped = list(word)
        swapped[i], swapped[i+1] = swapped[i+1], swapped[i]
        mutations.add("".join(swapped))

    return list(mutations)

# Example
# print(mutate("cat"))
