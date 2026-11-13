from itertools import combinations, product
from bisect import bisect_right

def solution(dice) :
    n = len(dice)
    m = n // 2
    dice_dict = {i : x for i, x in enumerate(dice)}
    max_a_win = 0
    answer = []

    for comb in combinations(range(n), m) :
        a_dice = [dice_dict[i] for i in comb]
        b_dice = [dice_dict[i] for i in range(n) if i not in comb]
        a_result = []
        for prod in product(range(6), repeat=m) :
            a_sum = 0
            for i, p in enumerate(prod) :
                a_sum += a_dice[i][p]
            a_result.append(a_sum)
        a_result.sort()
        a_win = 0
        cases = len(a_result)
        for prod in product(range(6), repeat=m) :
            b_sum = 0
            for i, p in enumerate(prod) :
                b_sum += b_dice[i][p]
            a_win += cases - bisect_right(a_result, b_sum)
        if a_win > max_a_win :
            max_a_win = a_win
            answer = [i + 1 for i in comb]

    return sorted(answer)

print(solution([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]))