s = open('z1-2.txt').read()
# s = 'XYYYXZYYZX'
n = len(s)
#0
d = [1 for i in range(n)]
#1
if s[0] != 'Y':
    d[0] = 0
#2
for i in range(1, n):
    if s[i] != 'Y':
        d[i] = 0
    elif s[i-1:i+1] == 'YY':
        d[i] = d[i-1] + 1
#3
print(max(d)) #10
