from itertools import product

words = [''.join(i) for i in product('аоу', repeat=5)]
print(words[209])
