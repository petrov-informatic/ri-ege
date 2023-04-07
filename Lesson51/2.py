def game(x, y, z, i, win_i, strategy=True):
    if x+y+z >= 71 or i > max(win_i):
        return i in win_i
    moves = [
        game(x+3, y, z, i+1, win_i, strategy),
        game(x, y+3, z, i+1, win_i, strategy),
        game(x, y, z+3, i+1, win_i, strategy),
        game(x*2, y, z, i + 1, win_i, strategy),
        game(x, y*2, z, i + 1, win_i, strategy),
        game(x, y, z*2, i + 1, win_i, strategy)
    ]
    if not strategy:
        return any(moves)
    if i % 2 == win_i[0] % 2:
        return all(moves)
    else:
        return any(moves)

r = range(1, 59)
print(f'19) {[s for s in r if game(7, 5, s, 0, [2], False)][0]}')
print(f'20) {[s for s in r if game(7, 5, s, 0, [3])]}')
print(f'21) {[s for s in r if game(7, 5, s, 0, [2, 4]) and not game(7,5,s,0,[2])]}')
