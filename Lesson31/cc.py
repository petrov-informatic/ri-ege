from string import ascii_lowercase


def cc(n, base):
    alf = ''.join([str(i) for i in range(10)])+ascii_lowercase #0123456789abcdefghigklmnopqqrstuvw
    a = '' if n > 0 else '0'
    while n:
        a = alf[n % base] + a
        n //= base
    return a
