n = int(input())
m1 = -float('inf')
m2 = -float('inf')
for i in range(n):
    a = int(input())
    if a > m1:
        m2 = m1
        m1 = a
print(m1, m2)