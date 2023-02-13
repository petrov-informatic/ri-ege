s = open('z4.txt').read()
# s = 'XYZXYXXXXYZXYZZXYZYYZZ'
# s = 'XY'
n = len(s)
#0
d = [0 for i in range(n)]
#1
if s[0] == 'X':
    d[0] = 1
#2
for i in range(1, n):
    if s[i-1:i+1] in 'XYZX' and d[i-1] > 0:
        d[i] = d[i-1] + 1
    elif s[i] == 'X':
        d[i] = 1
#3
print(max(d)) #13
