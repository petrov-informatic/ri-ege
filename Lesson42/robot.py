a = [[int(j) for j in i.split()] for i in open('file.txt').read().splitlines() if len(i)]
# a = [
#     [43, 47, 25, 35],
#     [49, 52, 83, 64],
#     [97, 8, 22, 32],
#     [36, 7, 85, 74]
# ]


def robot(function):
    m = len(a)
    n = len(a[0])
    d = [[0 for j in range(n)] for i in range(m)]
    d[0][0] = a[0][0]
    for i in range(1, m):
        d[i][0] = d[i - 1][0] + a[i][0] - 20
    for j in range(1, n):
        d[0][j] = d[0][j - 1] + a[0][j] - 15
    for i in range(1, m):
        for j in range(1, n):
            d[i][j] = function(a[i][j] + d[i][j - 1] - 15, a[i][j] + d[i - 1][j] - 20, a[i][j] + d[i - 1][j - 1] - 10)
    print(d[m - 1][n - 1])


robot(max)
robot(min)
