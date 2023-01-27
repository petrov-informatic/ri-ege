from string import ascii_lowercase


def cc(n, base):
    alf = ''.join([str(i) for i in range(10)])+ascii_lowercase #0123456789abcdefghigklmnopqqrstuvw
    a = '' if n > 0 else '0'
    while n:
        a = alf[n % base] + a
        n //= base
    return a


a = 5*343**8 + 4 * 49**12 + 7**14 - 98
a = cc(a, 7)
counts = [a.count(str(i)) for i in range(7)]
print(counts.index(max(counts)))
# m = 0
# x = None
# for i in range(7):
#     c = a.count(str(i))
#     if c > m:
#         m = c
#         x = i
# print(x)
