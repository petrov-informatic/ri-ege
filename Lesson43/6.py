d = [[0 for i in range(100)] for j in range(2)]
d[0][1] = 1
for i in range(2, 12):
    d[0][i] = d[0][i-1] + d[0][i-2]
    d[1][i] = d[1][i-1] + d[1][i-2] + (d[0][i//2] if i % 2 == 0 else 0) + (d[0][i//3] if i%3==0 else 0)
print(d[1][11])
