def time(id, z):
    for i in z:
        if i[0] == id:
            process = i
    if process[2][0] == '0':
        return process[1]
    sub_times = []
    for i in process[2]:
        sub_times.append(time(i, z))
    return max(sub_times) + process[1]


x = open('2.txt').read().splitlines()
x.pop(0)
y = []
for i in x:
    y.append(i.split('\t'))
for i in y:
    i[1] = int(i[1])
    i[2] = i[2].replace('"', '').split('; ')
times = []
for i in y:
    times.append(time(i[0], y))
print(max(times))

