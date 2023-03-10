def plus(x):
    # return int(str(int(str(x)[0])+1)+str(x)[1:])
    return x + 10**(len(str(x))-1)


def minus(x):
    if str(x)[0] != '1':
        return x - 10**(len(str(x))-1)
    if str(x)[0:2] == '10':
        return x - 10**(len(str(x))-2)
    return -1


def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    return f(x+1, y) + f(x*2, y) + f(2*x+1, y) + f(plus(x), y) + f(2*x-1, y)


d = [0 for i in range(200)]
d[7] = 1
for i in range(8, 78):
    d[i] = d[i-1] + (d[i//2] if i % 2 == 0 else d[(i-1)//2]+d[(i+1)//2]) + (d[minus(i)] if minus(i) != -1 else 0)
print(d[77])

# print(f(7,77))
#2488210
