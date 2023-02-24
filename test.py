s = open('file.txt').read()
d = [1 for i in s]
for i in range(1, len(s)):
    if s[i-1:i+1] not in 'LKL':
        d[i] = d[i-1] + 1
print(max(d))

