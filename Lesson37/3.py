s = open(input()+'.txt').read()
n = len(s)
alf = 'abcdefghijklmnopqrstuvwxyz'.upper()
counters = {key: 0 for key in alf}
for i in range(1, n-1):
    if s[i-1] == s[i+1]:
        counters[s[i]] += 1
mx = float('-inf')
t = None
for key in counters:
    if counters[key] > mx:
        mx = counters[key]
        t = key
print(t)
# D
