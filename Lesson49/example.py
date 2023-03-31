def game(x, i, win_i, func1=all, func2=any):
    if x >= 63 or i > max(win_i):
        return i in win_i
    return (func1 if i % 2 == win_i[0] % 2 else func2)([game(x+1, i+1, win_i), game(x+4, i+1, win_i), game(x*5, i+1, win_i)])


ans = {19: float('inf'), 20: [], 21: float('inf')}
for s in range(1, 63):
    if game(s, 0, [2], any, any):
        ans[19] = min(ans[19], s)
    if game(s, 0, [3]):
        ans[20].append(s)
    if game(s, 0, [2, 4]) and not game(s, 0, [2]):
        ans[21] = min(ans[21], s)
print(ans)



