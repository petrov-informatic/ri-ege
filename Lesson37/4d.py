s = open(input()+'.txt').read()
n = len(s)
d = [[0 for i in range(n)] for j in range(11)]
if s[0] == 'A':
    d[1][0] = 1
for i in range(1, n):
    if s[i] == 'A':
        d[1][i] = 1
    for j in range(2, 10):
        if s[i] != 'B' and s[i-1] != 'A':
            d[j][i] = d[j-1][i-1]
        elif s[i-1] == 'A' and j == 2 and s[i] != 'B':
            d[j][i] = 1
    if s[i-1] != 'A' and s[i] != 'B':
        d[10][i] = int(d[9][i-1] or d[10][i-1])
print(sum([d[10][i] for i in range(n) if s[i] == 'A']))
