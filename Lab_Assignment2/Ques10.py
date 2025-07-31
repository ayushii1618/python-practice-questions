def wrap_file(filename, width):
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            for i in range(0, len(line), width):
                print(line[i:i+width])

# Example
wrap_file("sample.txt", 10)
