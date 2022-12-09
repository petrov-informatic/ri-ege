# def alg(n):
#     def digits_sum(s):
#         s1 = 0
#         for i in range(len(s)):
#             s1 += int(s[i])
#         return s1
#     n = str(n)
#     d135 = n[::2]
#     d24 = n[1::2]
#     s1 = digits_sum(d135)
#     s2 = digits_sum(d24)
#     return int(f'{min(s1,s2)}{max(s1,s2)}')

def alg(n):
    s1, s2 = 0, 0
    for i, digit in enumerate(str(n)):
        if i % 2:
            s1 += int(digit)
        else:
            s2 += int(digit)
    return int(f'{min(s1,s2)}{max(s1,s2)}')


for j in range(10000, 100000):
    if alg(j) == 723:
        print(j)
        break

