a = [int(i) for i in open(f'{input()}.txt').read().splitlines()]
n = a.pop(0)

print(a, n)
