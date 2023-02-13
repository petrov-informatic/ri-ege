s = open('z1-2.txt').read()
# s = 'XYYYXZYYZX'
n = len(s)
counter = 0
mx = float('-inf')
for si in s:
    if si == 'Y':
        counter += 1
    else:
        mx = max(mx, counter)
        counter = 0
print(mx) #10

