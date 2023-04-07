def get_first_last(array):
    return [array[0], array[-1]]


def game(x, y, i, win_i):
    if x + y <= 32 or i > max(win_i):
        return i in win_i
    return (all if i % 2 == win_i[0] % 2 else any)([
        game(x-1, y, i+1, win_i),
        game(x, y-1, i+1, win_i),
        game((x+1)//2, y, i+1, win_i),
        game(x, (y+1)//2, i+1, win_i)
    ])


print(f'19: {[s for s in range(23, 1000) if game(s, 10, 0, [2])]}')
print(f'20: {get_first_last([s for s in range(23, 1000) if game(s, 10, 0, [3])])}')
print(f'21: {[s for s in range(23, 1000) if game(s, 10, 0, [2, 4]) and not game(s, 10, 0, [2])]}')
#19: 45
#20: 4690
#21: 48