from itertools import product

words = [''.join(i) for i in product('агилморт', repeat=4)]
# i1 = words.index('гоаа')
# i2 = words.index('ттго')
firstFound = False
for i, word in enumerate(words):
    if word[-2:] == 'го':
        i2 = i
    if word[:2] == 'го':
        if not firstFound:
            i1 = i
            firstFound = True

print(i2-i1-1)
