def f(a, b):
    return a[0] if b != a[0] else a[1]


s = open('dz37.5.txt').read()
n = len(s)
d = {k: {j: [0 for i in s] for j in range(1, 4)} for k in ['A', 'B', 'C', 'AB', 'AC', 'BC']}
d[s[0]][1][0] = 1
for i in range(1, n):
    d[s[i]][1][i] = 1
    d[s[i]][2][i] = d[s[i]][1][i-1]
    d[s[i]][3][i] = d[s[i]][2][i-1]+d[s[i]][3][i-1]
    for k in ['AB', 'BC', 'AC']:
        if set(s[i-1:i+1]) == set(k):
            d[k][2][i] = 1
        if s[i] in k:
            d[k][3][i] = d[k][2][i-1]+d[k][3][i-1]+d[f(k, s[i])][3][i-1]+d[f(k, s[i])][2][i-1]
print(sum([d[k][3][i] for i in range(n) for k in d]))
#252776
