def min_max(array): return [array[0], array[-1]]


def game(x, y, i, win_is):
    if x + y >= 45 or i > max(win_is):
        return i in win_is
    return (all if i % 2 == win_is[0] % 2 else any)([
        game(x+2, y, i+1, win_is),
        game(x, y+2, i+1, win_is),
        game(x*3, y, i+1, win_is),
        game(x, y*3, i+1, win_is)
    ])


r = range(1, 44)
print(f'19) {len([[k, s] for k in r for s in r if game(k, s, 0, [2]) and s + k <= 43])}')
print(f'20) {min_max([s for s in r if game(4, s, 0, [3]) and s + 4 <= 43])}')
print(f'21) {[s for s in r if game(13, s, 0, [2, 4]) and not game(13, s, 0, [2]) and s + 13 <= 43]}')