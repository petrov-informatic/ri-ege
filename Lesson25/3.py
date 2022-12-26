from itertools import product

words = [''.join(i) for i in product('апрсу', repeat=3)]
# for j, word in enumerate(words):
#     if word[0] == 'с':
#         print(j)
#         break
print(words.index('саа'))
