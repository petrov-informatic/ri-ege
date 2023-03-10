def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    return f(x+1, y) + f(x*2, y) + f(x*3, y)


print(f(1, 13))


d = [1 for i in range(27)]
for i in range(2, 14):
    d[i] = d[i-1] + (d[i//2] if i % 2 == 0 else 0) + (d[i//3] if i % 3 == 0 else 0)
print(d[13])

