def del_two(x):
    return int(str(x)[1:])


d = [0 for i in range(1000)]
d[3] = 1
for i in range(4, 679):
    d[i] = d[i-1] + (d[del_two(i)] if str(i)[0] == '2' and str(i)[1] != '0' else 0)
print(d[678])
