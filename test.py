def rreplace(s, old, new, count=-1):
    return s[::-1].replace(old[::-1], new[::-1], count)[::-1]


print('bcaaaa'.replace('aa', 'b', 1))
print(rreplace('bcaaaa', 'aa', 'b'))
# bcaab