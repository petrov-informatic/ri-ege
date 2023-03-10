def f(x,y):
    if x == y:
        return 1
    if x < y:
        return 0
    return f(x-1, y) + f(x//2, y)


print(f(30, 12) * f(12, 1))
#376


def g(x, y):
    d = [0 for i in range(100)]
    d[x] = 1
    for i in range(x-1, y-1, -1):
        d[i] = d[i+1] + d[2*i] + d[2*i+1]
    return d[y]


print(g(30,12) * g(12, 1))


d = [[0 for i in range(100)] for j in range(100)]
for i in range(len(d)):
    d[i][i] = 1
for j in range(100):
    for i in range(j-1, -1, -1):
        d[j][i] = d[j][i+1] + (d[j][i*2] if 2*i<100 else 0) + (d[j][i*2+1] if 2*i+1<100 else 0)
print(d[30][12] * d[12][1])
