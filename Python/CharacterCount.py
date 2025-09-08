"""
Count the character in a string, should not count symbols and white spaces, Only lowercase english letters are given.
Input: hello hii
Output:
h - 2
e - 1
l - 2
o - 1
i - 2.
"""

inp = "How are you?"

hashMap = {}

for char in inp:
    if char == " ":
        continue
    hashMap[char] = hashMap.get(char, 0) + 1

for item in hashMap:
    print(f"{item} - {hashMap[item]}")