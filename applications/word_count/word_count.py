def word_count(s):
    counts = {}
    words = s.lower().split()
    ignoring = '":;,.-+=/\\|[]{}()*^&'

    for word in words:
        for i in ignoring:
            if i in word:
                word = word.replace(i, '')
        if word in counts:
            counts[word] += 1
        else:
            if len(word) > 0:
                counts[word] = 1

    return counts

print(word_count('This is a test of the emergency broadcast network. This is only a test.'))

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))