s = open('int104.txt').read()
n = len(s)
d = [[0 for i in range(n)] for j in range(5)]
if s[0] == '.':
    d[1][0] = 1
else:
    d[0][0] = 1
for i in range(1, n):
    if s[i] != '.':
        d[0][i] = d[0][i-1] + 1
    for j in range(1, 5):
        d[j][i] = d[j-1][i-1]+1 if s[i] == '.' else d[j][i-1]+1
print(max([d[j][i] for j in range(5) for i in range(n)]))
