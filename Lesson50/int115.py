s = open('file.txt').read()
n = len(s)
d = [[0 for i in range(n)] for j in range(3)]
if s[0].isalpha():
    d[0][0] = 1
for i in range(1, n):
    if s[i].isalpha():
        d[0][i] = d[2][i-1]+1
        if d[1][i-1] > 0:
            d[2][i] = d[1][i-1] + 1
    if s[i].isdigit() and d[0][i-1] > 0:
        d[1][i] = d[0][i-1] + 1
print(max(d[2])//3)
