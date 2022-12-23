from itertools import product


def good(word):
    return word.count('С') == 1


words = [''.join(i) for i in product('СЛОН', repeat=5)]
count = 0
for word in words:
    if good(word):
        count += 1
print(count)