from collections import defaultdict

def find_anagrams(words):
    anagram_groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        anagram_groups[key].append(word)
    return [group for group in anagram_groups.values() if len(group) > 1]

# Example
print(find_anagrams(["eat", "tea", "ate", "bat", "tab", "tan"]))
