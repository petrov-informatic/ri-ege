def divs(x):
    # d = []
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            if i % 2:
                d.add(i)
                # d.append(i)
            j = x // i
            # if i != j and j % 2:
            if j % 2:
                d.add(j)
                # d.append(j)
    return d


for i1 in range(55000000, 60000000+1):
    d1 = divs(i1)
    if len(d1) == 5:
        print(i1, max(d1))
