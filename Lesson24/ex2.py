def good(n):
    return int(n) in range(100, 1000) and int(n) % 2 == 0


s = '0123456'
count = 0
for i1 in s:
    for i2 in s:
        for i3 in s:
            number = i1+i2+i3
            if good(number):
                count += 1
print(count)
