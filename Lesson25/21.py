def alg(s):
    while '222' in s or '888' in s:
        if '222' in s:
            s = s.replace('222', '8', 1)
        else:
            s = s.replace('888', '2', 1)
    return s


st = '8'*68

print(alg(st))
