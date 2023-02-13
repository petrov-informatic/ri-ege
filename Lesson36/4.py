s = open('z4.txt').read()
# s = 'XYZXYXXXXYZXYZZXYZYYZZ'
# s = 'XY'
n = len(s)
counter = 0
mx = float('-inf')
s = s.replace('XYZ', '1').replace('1XY', '10').replace('1X', '12')
for i in s:
    if i == '1':
        counter += 3
    elif i == '0':
        counter += 2
        mx = max(mx, counter)
        counter = 0
    elif i == '2':
        counter += 1
        mx = max(mx, counter)
        counter = 0
    else:
        mx = max(mx, counter)
        counter = 0
print(mx) #13
