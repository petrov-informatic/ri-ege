d = [0 for i in range(100)]
d[2] = 1
for i in range(3, 51):
    d[i] = d[i-2] + (d[i//5] if i % 5 == 0 else 0)
print(d[50])


def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    return f(x + 2, y) + f(x * 5, y)


print(f(2,50))
