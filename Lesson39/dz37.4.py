s = open('dz37.4.txt').read()
n = len(s)
d = [0 for i in s]
if s[0].isalpha():
    d[0] = 1
for i in range(1, n):
    if d[i-1] > 0 and s[i].isalpha() != s[i-1].isalpha():
        d[i] = d[i-1] + 1
    elif s[i].isalpha():
        d[i] = 1
print(1/2*max([d[i] for i in range(n) if s[i].isdigit()]))
#183
