s = input()
f = 'f'
firstIndex = s.find(f)
if f not in s:
    print('NO')
elif s.count(f) == 1:
    print(firstIndex)
else:
    print(firstIndex, s.rfind(f))
