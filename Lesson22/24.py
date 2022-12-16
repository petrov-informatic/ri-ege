s = open('24file.txt').read()
n = len(s)
d = [1 for i in range(n)]
for i in range(1, n):
    if s[i-1:i+1] in ['ad', 'da']:
        d[i] = 1
    else:
        d[i] = d[i-1] + 1
print(max(d))
