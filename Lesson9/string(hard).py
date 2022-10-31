s = input()
if '.' in s:
    pointIndex = s.find('.')
    digit = s[pointIndex+1]
else:
    digit = '0'
print(digit)
