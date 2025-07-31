def file_stats(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)
    return num_chars, num_words, num_lines

# Example
print("Stats:", file_stats("sample.txt"))
