s = open('z1-2.txt').read()
n = len(s)
d = [1 for i in range(n)]
for i in range(1, n):
    if s[i] != s[i-1]:
        d[i] = d[i-1] + 1
print(max(d)) #35
