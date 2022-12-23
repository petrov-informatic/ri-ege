from itertools import permutations


s = 'георгий'
n = list(set([''.join(i) for i in permutations(s, 7)]))
count = 0
for word in n:
    if 'гг' not in word:
        count += 1
print(count)
