from itertools import product


def good(word):
    word = word.replace('П', 'Т').replace('Я', 'Е')
    return 'ТТ' not in word and 'ЕЕ' not in word


count = 0
for i in product('ПЕТЯ', repeat=6):
    tmp = ''.join(i)
    if good(tmp):
        count += 1
print(count)
