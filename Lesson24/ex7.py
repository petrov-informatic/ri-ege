from itertools import product


def good(word):
    return word.count('X')==1 and word[-1] == 'X' or 'X' not in word


words = [''.join(i) for i in product('ABCX', repeat=5)]
count = 0
for word in words:
    if good(word):
        count += 1
print(count)

