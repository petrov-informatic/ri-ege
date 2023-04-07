def game(x, y, i, win_i):
    if x+y >= 40 or i > max(win_i):
        if x+y <= 49:
            return i in win_i
        else:
            return i+1 in win_i
    moves = [
        game(x+1, y, i+1, win_i),
        game(x*2, y, i + 1, win_i),
        game(x, y+1, i + 1, win_i),
        game(x, y*2, i + 1, win_i)
    ]
    return (all if i % 2 == win_i[0] % 2 else any)(moves)


r = range(1, 25+1)
print(f'19) {[s for s in r if game(14, s, 0, [2]) and not game(14, s, 0, [1])]}')
print(f'20) {[s for s in r if game(14, s, 0, [3]) and not game(14, s, 0, [1])]}')
print(f'21) {[s for s in r if game(14, s, 0, [2, 4]) and not game(14, s, 0, [2])]}')

