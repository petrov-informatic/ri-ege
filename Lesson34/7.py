a = [int(i) for i in open(input()+'.txt').read().splitlines()]
n = len(a)

max151 = max([i for i in a if i % 151 == 0])
sums = []
for i in range(n-1):
    if (a[i] > max151 or a[i+1] > max151) and ('3' in hex(a[i]) or '3' in hex(a[i+1])):
        sums.append(a[i]+a[i+1])
print(len(sums), min(sums))
# 15 12582
