def f(x,y):
    if x == y:
        return 1
    if x < y:
        return 0
    return f(x-2, y) + f(x-5, y) + f(x//2, y)


print(f(22,2))
#127

d = [0 for i in range(100)]
d[22] = 1
for i in range(21, 2-1, -1):
    d[i] = d[i+2]+d[i+5]+d[2*i]+d[2*i+1]
print(d[2])
