from collections import Counter

def char_frequency(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return Counter(text)

# Heuristic detection based on special chars
def detect_file_type(filename):
    freq = char_frequency(filename)
    content = ''.join(freq.keys())
    if '#' in content and 'include' in content:
        return "C Program File"
    elif 'def' in content or 'import' in content:
        return "Python Program File"
    else:
        return "Text File"

# Example
# print(detect_file_type("sample.txt"))
