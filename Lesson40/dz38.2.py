def divs(n):
    i = 1
    d1 = []
    d2 = []
    while i**2 <= n:
        if n % i == 0:
            if i % 2 == 0:
                d1.append(i)
            if (n // i) % 2 == 0 and n // i != i:
                d2.append(n // i)
        i += 1
    return d1 + d2[::-1]


for j in range(110203, 110245+1):
    b = divs(j)
    if len(b) == 4:
        print(j, *b)
