import random

with open("input.txt") as f:
    words = f.read()

split_words = words.split()

dataset = {}

for i in range(len(split_words) - 1):
    word = split_words[i]
    next_word = split_words[i + 1]

    if word not in dataset:
        dataset[word] = [next_word]

    else:
        dataset[word].append(next_word)

start_words = []
for key in dataset.keys():
    if key[0].isupper() or (len(key) > 1 and key[1].isupper()):
        start_words.append(key)

for i in range(5):

    word = random.choice(start_words)

    stopped = False

    stop_signs = "?.!"

    while not stopped:
        print(word, end=" ")
        if word[-1] in stop_signs or len(word) > 1 and word[-2] in stop_signs:
            stopped = True

        following_words = dataset[word]
        word = random.choice(following_words)
    
    print("")