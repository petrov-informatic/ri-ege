from itertools import product

def good(n):
    return n[0] in 'ЕЭ'


s = 'ЕГЭ'
words = [''.join(i) for i in product(s, repeat=5)]
count = 0
for word in words:
    if good(word):
        count += 1
print(count)

# s = 'ЕГЭ'
# count = 0
# for i1 in s:
#     for i2 in s:
#         for i3 in s:
#             for i4 in s:
#                 for i5 in s:
#                     word = i1+i2+i3+i4+i5
#                     if good(word):
#                         count += 1
# print(count)
