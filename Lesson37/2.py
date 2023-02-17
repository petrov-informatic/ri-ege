s = open(input()+'.txt').read()
n = len(s)
alf = 'abcdefghijklmnopqrstuvwxyz'.upper()
# counters = {key: 0 for key in alf}
counters = [0 for i in alf]
for i in range(1, n):
    if s[i-1] == 'A':
        # counters[s[i]] += 1
        counters[alf.find(s[i])] += 1
# vals = list(counters.values())
# print(list(counters.keys())[vals.index(max(vals))])
# G
print(alf[counters.index(max(counters))])


