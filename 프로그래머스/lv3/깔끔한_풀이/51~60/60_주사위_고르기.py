from itertools import combinations, product
from bisect import bisect_right

def solution(dice):
    n = len(dice)
    m = n // 2
    max_a_win = 0
    answer = []

    for comb in combinations(range(n), m):
        a_dice = [dice[i] for i in comb]
        b_dice = [dice[i] for i in range(n) if i not in comb]
        
        # 1. A의 모든 합을 구하고 바로 정렬 (generator expression 활용)
        a_result = sorted(
            sum(a_dice[i][p] for i, p in enumerate(prod)) 
            for prod in product(range(6), repeat=m)
        )
        
        # 2. B의 모든 합을 구하면서 A의 승리 횟수 계산
        a_win = 0
        cases = len(a_result)
        for prod in product(range(6), repeat=m):
            b_sum = sum(b_dice[i][p] for i, p in enumerate(prod))
            a_win += cases - bisect_right(a_result, b_sum)
            
        # 3. 최대 승리 횟수 갱신
        if a_win > max_a_win:
            max_a_win = a_win
            answer = [i + 1 for i in comb]

    return sorted(answer)