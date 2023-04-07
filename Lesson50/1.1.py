def game(x, i, win_i, func1=all, func2=any):
    if x > 37 or i > max(win_i):
        return i in win_i
    return (func1 if i % 2 == win_i[0] % 2 else func2)([
        game(x+1,i+1,win_i,func1, func2),
        game(x+2,i+1, win_i, func1, func2),
        game(x*2, i+1, win_i, func1, func2)
    ])


r = range(1, 38)
ans = {
    19: min([s for s in r if game(s, 0, [2], any)]),
    20: [s for s in r if game(s, 0, [3])],
    21: min([s for s in r if game(s, 0, [2, 4]) and not game(s, 0, [2])])
}
print(ans)
