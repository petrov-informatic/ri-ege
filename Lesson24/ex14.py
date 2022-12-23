from itertools import product


def good(word):
    c1 = word.count('В') <= 1
    c2 = word[0] != 'Ш'
    c3 = word[-1] not in 'ИЯ'
    return c1 and c2 and c3


s = 'ВИШНЯ'
count = 0
for i in product(s, repeat=6):
    word = ''.join(i)
    if good(word):
        count += 1
print(count)
