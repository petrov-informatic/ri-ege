from itertools import product


def good(word):
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            return False
    return word[0] != 'а' # and 'аа' not in word and 'бб' not in word and 'вв' not in word and 'гг' not in word and 'дд' not in word


words = [1 for i in product('абвгд', repeat=6) if good(''.join(i))]
print(len(words))
