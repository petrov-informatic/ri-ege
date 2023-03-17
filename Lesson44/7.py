def s(x):
    return sum([int(i) for i in str(x)])


def f(x, y, count):
    if x == y and count == 5:
        return 1
    if x >= y:
        return 0
    return f(x+2, y, count+1 if s(x+2) == 14 else count) + f(x*3, y, count+1 if s(x*3) == 14 else count) + f(x*4, y, count+1 if s(x*4) == 14 else count)


print(f(1, 600, 0))
