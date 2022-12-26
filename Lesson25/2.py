from itertools import product

words = [''.join(i) for i in product('АКРУ', repeat=5)]
print(words[349])
