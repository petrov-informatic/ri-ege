def is_prime(x):
    i = 2
    while i ** 2 <= x:
        if x % i == 0:
            return False
        i += 1
    return True


def prime_table(a):
    t = []
    for i in range(2, a+1):
        if is_prime(i):
            t.append(i)
    return t


count = 0
mn = float('inf')
mni = None
a, b = 153732, 225674
pt = prime_table(b//2)
for p in pt:
    for q in pt:
        if p!=q and p*q in range(a, b+1):
            count += 1
            if abs(p-q) < mn:
                mn = abs(p-q)
                mni = p*q
print(count, mni)
