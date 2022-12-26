def alg(s):
    while '1111' in s:
        s = s.replace('1111', '22', 1).replace('222', '1', 1)
    return s


for n in range(201, 300):
    st = '1'*n
    if alg(st).count('1') == 0:
        print(n)
        break
