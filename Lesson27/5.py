# n = int(input())
# a = []
# for i in range(n):
#     a.append(int(input()))
a = [int(input()) for i in range(int(input()))]
# b = []
# for i in range(len(a)-1):
#     b.append(sum(a[i:i+2]))
# print(b)
print([sum(a[i:i+2]) for i in range(len(a)-1)])
