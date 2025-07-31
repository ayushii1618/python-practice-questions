# Writing to a file
with open("sample.txt", "w") as f:
    f.write("Hello World!\n")
    f.writelines(["This is line 1\n", "This is line 2\n"])

# Reading from the file
with open("sample.txt", "r") as f:
    print("Full content:\n", f.read())

# Reading line-by-line
with open("sample.txt", "r") as f:
    print("First line:", f.readline())
