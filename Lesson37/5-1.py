s = open(input()+'.txt').read()
n = len(s)
s = s.replace('AB', '2').replace('CAC', '3')
for sym in 'ABC':
    s = s.replace(sym, '0')
s = [sum([int(j) for j in i]) for i in s.split('0') if len(i)]
print(max(s))

