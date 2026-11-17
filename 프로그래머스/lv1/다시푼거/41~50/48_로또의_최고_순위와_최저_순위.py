def solution(lottos, win_nums):
    rank = {0 : 6, 1 : 6, 2 : 5, 3 : 4, 4 : 3, 5 : 2, 6 : 1}
    zero = lottos.count(0)
    base = 0
    for l in lottos :
        if l in win_nums :
            base += 1
    return [rank[base + zero], rank[base]]