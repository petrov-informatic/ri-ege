from itertools import product

def good(word):
    return word[0] in 'ЗМ' and word[-1] in 'ИА'


n = 'ЗИМА'
words = [''.join(i) for i in product(n, repeat=5)]
count = 0
for word in words:
    if good(word):
        count += 1
print(count)
