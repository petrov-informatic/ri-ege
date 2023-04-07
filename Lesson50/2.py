def game(x, i, win_i):
    if x > 49 or i > max(win_i):
        return i in win_i
    return (all if i % 2 == win_i[0] % 2 else any)([game(x+2,i+1,win_i), game(x*3, i+1, win_i)])


r = range(1, 50)
ans = {
    19: min([s for s in r if game(s, 0, [2])]),
    20: len([s for s in r if game(s, 0, [3])]),
    21: [s for s in r if game(s, 0, [2, 4]) and not game(s, 0, [2])][-2:]
}
print(ans)
#19: 15
#20: 3
#21: 1112