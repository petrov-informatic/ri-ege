def f(x, y, flag):
    if x == y and not flag:
        return 1
    if x >= y:
        return 0
    return f(x+2, y, x % 2 == (x+2) % 2 == 1 or flag) + f(x*3, y, x % 2 == (x*3)%2 == 1 or flag) + f(x*4, y, x % 2 == (x*4)%2 == 1 or flag)


def g(x):
    if x == 600:
        return 1
    if x > 600:
        return 0
    return g(x+2) + g(x*3) + g(x*4)


print(f(1, 600, 0)) #58253
print(g(4))
