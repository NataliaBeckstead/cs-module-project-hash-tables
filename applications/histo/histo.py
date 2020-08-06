

with open("robin.txt") as f:
    words_from_file = f.read()

counts = {}
longest_word_length = 0

def word_count(s):
    words = s.lower().split()
    ignoring = '":;,.-+=/\\|[]{}()*^&!?'
    for word in words:
        for i in ignoring:
            if i in word:
                word = word.replace(i, '')
        global longest_word_length
        if len(word) > longest_word_length:
            longest_word_length = len(word)
        if word in counts:
            counts[word] += 1
        else:
            if len(word) > 0:
                counts[word] = 1
    return counts

word_count(words_from_file)

histo = {}

for key in counts:
    spaces = longest_word_length + 2 - len(key)
    if counts[key] in histo:
        histo[counts[key]].append(key + " " * spaces + ("#" * counts[key]))
    else:
        histo[counts[key]] = []
        histo[counts[key]].append(key + " " * spaces + ("#" * counts[key]))

#sorted_letter_counts = sorted(letter_counts.items(), key=lambda pair: pair[1], reverse=True)
sorted_histo = dict(sorted(histo.items(), reverse=True))

for i in sorted_histo:
    sorted_histo[i].sort()
    for j in sorted_histo[i]:
        print(j)
