import re

with open("ciphertext.txt") as f:
    encoded = f.read()

cracking_key = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

counter = {}

for char in encoded:
    if re.match(r'[a-zA-Z]', char):
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

# sorting by value from biggest to smallest
counter = {k: v for k,v in sorted(counter.items(), key=lambda x: x[1], reverse=True)}

# crating a list with letters sorted by appearance
counter_list = []
for key in counter:
    counter_list.append(key)

# creating decoded text
# if letter - add a letter from same index in a cracking key, else add same symbol
decoded = ""

for char in encoded:
    if char in counter_list:
        index = counter_list.index(char)
        decoded += cracking_key[index]
    else:
        decoded += char

print(decoded)