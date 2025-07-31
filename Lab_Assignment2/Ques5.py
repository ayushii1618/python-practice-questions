# Sort by length
def lensort(strings):
    return sorted(strings, key=len)

# Sort by file extension
def extsort(files):
    return sorted(files, key=lambda x: x.split('.')[-1])

# Example
words = ["banana", "pie", "apple", "kiwi"]
files = ["doc.txt", "photo.jpg", "notes.pdf", "data.csv"]

print("Sorted by length:", lensort(words))
print("Sorted by extension:", extsort(files))
