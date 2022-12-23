def good(n):
    for i in '15678':
        if n.count(i) > 1:
            return False
    return True

s = '15678'
count = 0
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                number = i1+i2+i3+i4
                if good(number):
                    count += 1
print(count)