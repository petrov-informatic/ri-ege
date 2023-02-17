s = open(input()+'.txt').read()
n = len(s)
s = s.replace('AB', '2').replace('CAC', '3')
for sym in 'ABC':
    s = s.replace(sym, '0')
mx = float('-inf')
counter = 0
for i in s:
    if i != '0':
        counter += int(i)
    else:
        mx = max(mx, counter)
        counter = 0
print(mx)


