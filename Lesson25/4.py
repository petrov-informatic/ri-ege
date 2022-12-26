from itertools import product


def good(word):
    return word.count('в') == 1


alf = 'вероника'
words = [''.join(i) for i in product(alf, repeat=3) if good(''.join(i))]
words.sort()
# for i, word in enumerate(words):
#     if 'а' not in word:
#         print(i)
#         break
print(words.index('вее'))