a = [[int(j) for j in i.split()] for i in open('file.txt').read().splitlines()]
n = a.pop(0)[0]

print(a, n)
