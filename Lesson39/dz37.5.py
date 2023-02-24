# s = 'ABCCBABC'
s = open('dz37.5.txt').read()
a = 0
b = 0
c = 0
count = 0
n = len(s)
for i in range(n):
    for j in range(i, n):
        if s[j] == 'A':
            a += 1
        if s[j] == 'B':
            b += 1
        if s[j] == 'C':
            c += 1
        if a*b*c == 0:
            if j - i >= 2:
                count += 1
        else:
            a, b, c = 0, 0, 0
            break
print(count)
# 252776
