def divs(x):
    i = 2
    d = set()
    while i**2 <= x:
        if x % i == 0:
            d.add(i)
            d.add(x // i)
        i += 1
    return d


for i in range(135790, 163228+1):
    d = divs(i)
    if sum(d) > 460000:
        print(len(d), sum(d))
