def to(n, base):
    s, digits = '', '0123456789abcdef'
    while n > 0:
        s = f'{digits[n % base]}{s}'
        n //= base
    return s
