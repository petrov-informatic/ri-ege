s = open(input()+'.txt').read()
n = len(s)
s = s.split('A')
count = 0
for i in s:
    if len(i) >= 8 and ('B' not in i):
        count += 1
print(count)
