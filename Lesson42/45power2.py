def good(x):
    if x % 3 == 0 or x % 7 == 0:
        return False
    while x % 20 == 0:
        x //= 20
    while x % 5 == 0:
        x //= 5
    while x % 4 == 0:
        x //= 4
    return x == 1


count = 0
r = range(2*10**8, 6*10**8+1)
for i in r:
    if good(i):
        count += 1
print(count)
