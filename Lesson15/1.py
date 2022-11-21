for N in range(256):
    N0 = N
    N = bin(N)[2:]
    if len(N) < 8:
        N = '0' * (8 - len(N)) + N
    N = N.replace('0','2').replace('1', '0').replace('2', '1')
    N = int(N, 2)
    if 133 == N - N0:
        print(N0)
