from itertools import permutations


def good(word):
    for i in range(len(word)-1):
        if word[i] in 'аие' and word[i+1] in 'аие':
            return False
    return True


# words = [1 for i in permutations('здание') if good(''.join(i))]
# print(len(words))

words = [''.join(i) for i in permutations('здание')]
c = 0
for word in words:
    if good(word):
        c += 1
print(c)
