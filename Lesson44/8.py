def s(x):
    return sum([int(i) for i in str(x)])


def p(x):
    t = 1
    while x > 0:
        t *= x % 10
        x //= 10
    return t


def f(x):
    if x == 8:
        return True
    if x < 10:
        return False
    return f(s(x)) or f(p(x))


count = 0
for i in range(10,100):
    if f(i):
        count += 1
print(count)
