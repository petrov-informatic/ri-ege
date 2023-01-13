from itertools import permutations


def alg(s):
    while '11' in s:
        if '112' in s:
            s = s.replace('112', '6', 1)
        else:
            s = s.replace('11', '3', 1)
    return s


def sum_digits(n):
    s = 0
    for i in n:
        s += int(i)
    return s


strings = list(set([''.join(i) for i in permutations('1'*10+'222')]))
m = 0
for string in strings:
    m = max(m, sum_digits(alg(string)))
print(m)
