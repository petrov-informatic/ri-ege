def is_prime(x):
    i = 2
    while i**2 <= x:
        if x % i == 0:
            return False
        i += 1
    return True


count = 0
mn = float('inf')
mni = None
for i in range(153732, 225674+1):
    p = []
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            p.append(j)
            p.append(i // j)
    if len(p) == 2 and is_prime(p[0]) and is_prime(p[1]):
        count += 1
        if p[1]-p[0] < mn:
            mn = p[1] - p[0]
            mni = i
print(count, mni)
# 15549 157609

