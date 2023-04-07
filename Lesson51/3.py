def game(x, i, win, last_move=None):
    if x >= 140 or i > max(win):
        return i in win
    moves = [
        game(x+1, i+1, win, 0),
        game(x+2, i+1, win, 1),
        game(x*3, i+1, win, 2)
    ]
    if i > 0:
        moves.pop(last_move)
    return (all if i % 2 == win[0] % 2 else any)(moves)


r = range(1, 139+1)
print(f'19) {[s for s in r if game(s, 0, [2])]}')
print(f'20) {[s for s in r if game(s, 0, [3])]}')
print(f'21) {[s for s in r if game(s, 0, [2, 4]) and not game(s, 0, [2])]}')
