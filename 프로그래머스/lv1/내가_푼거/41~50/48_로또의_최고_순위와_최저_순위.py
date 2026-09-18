def solution(lottos, win_nums):
    lotto_rank = {0 : 6, 1 : 6, 2 : 5, 3 : 4, 4 : 3, 5 : 2, 6 : 1}
    s = set(i for i in lottos if i != 0)
    minimum = len(s & set(win_nums))

    answer = [lotto_rank[6 - len(s) + minimum], lotto_rank[minimum]]
    return answer

# print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))