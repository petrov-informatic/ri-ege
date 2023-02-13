s = open('z1-2.txt').read()
counter = 1
mx = float('-inf')
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        counter += 1
    else:
        mx = max(mx, counter)
        counter = 1
print(mx) #35

