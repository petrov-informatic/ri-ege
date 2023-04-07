a = [int(i) for i in open(input()).read().splitlines()]
n, k = a.pop(0), a.pop(0)
d = [float('-inf') for i in range(n)]
for i in range(k, n):
    d[i] = max(d[i-1], a[i-k])
print(max([d[i]+a[i] for i in range(n)]))


# mx = float('-inf')
# for i in range(n):
#     for j in range(i+1, n):
#         if j-i >= k and a[i]+a[j] > mx:
#             mx = a[i] + a[j]
# print(mx)


