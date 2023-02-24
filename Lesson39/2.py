def is_prime(x):
    i = 2
    while i**2 <= x:
        if x % i == 0:
            return False
        i += 1
    return True


def M(x):
    divs = []
    i = 2
    while i**2 <= x:
        if x % i == 0:
            if is_prime(i):
                divs.append(i)
            if is_prime(x // i):
                divs.append(x // i)
        i += 1
    return max(divs) - min(divs) if len(divs) else 0


count = 0
i = 450000+1
while count < 4:
    M_ = M(i)
    if M_ % 29 == 11:
        count += 1
        print(i, M_)
    i += 1
