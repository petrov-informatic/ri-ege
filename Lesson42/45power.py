end = 6*10**8
r = range(2*10**8, end+1)


def find_max(base):
    mx = 0
    while base**mx <= end:
        mx += 1
    return mx


m_max = find_max(4)
n_max = find_max(5)
count = 0
for n in range(n_max+1):
    for m in range(m_max+1):
        N = 4**m * 5**n
        if N in r:
            count += 1
print(count, n_max, m_max)
