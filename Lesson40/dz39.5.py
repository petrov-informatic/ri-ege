from time import time


def mask(a, b):
    return int(f'12{a}45{b}')


def match(n):
    n = str(n)
    return n.find('12') == 0 and n.find('45') >= 2

t0 = time()
star = [""] + [str(i) for i in range(10)] + [f'{i}{j}' for i in range(10) for j in range(10)]
a = []
for star1 in star:
    for star2 in star:
        m = mask(star1, star2)
        if m <= 10**6 and m % 51 == 0:
            a.append(m)
a.sort()
for i in a:
    print(i, i // 51)
t1 = time()

for i in range(1000, 10**6+1):
    if match(i) and i % 51 == 0:
        print(i, i // 51)
t2 = time()
print(t1-t0, t2-t1)