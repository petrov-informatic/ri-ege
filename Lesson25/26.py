from random import shuffle

def isprime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def alg(s):
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1','22>',1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    return s


def summ(s):
    c = 0
    for i in s:
        if i != '>':
            c += int(i)
    return c


for n in range(100):

    st = '>'+39*'0'+n*'1'+39*'2'
    if isprime(summ(alg(st))):
        print(n)
        break
