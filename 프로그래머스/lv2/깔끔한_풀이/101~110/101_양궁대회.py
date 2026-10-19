from itertools import combinations_with_replacement

def solution(n, info):
    max_score_arrows = [-1]
    max_score = 0
    
    for case in combinations_with_replacement(range(11), n):
        current_arrow = [0] * 11
        for i in case:
            current_arrow[10 - i] += 1
            
        score = 0
        for i in range(11):
            if current_arrow[i] > info[i]:
                score += (10 - i)  # 라이언이 이긴 경우 (점수 획득)
            elif info[i] > 0:
                score -= (10 - i)  # 어피치가 이긴 경우 또는 비긴 경우(어피치 획득)
                
        if score > max_score:
            max_score = score
            max_score_arrows = current_arrow[:]  # 안전하게 복사
        elif score > 0 and score == max_score:
            # 점수 차이가 같다면, 가장 낮은 점수(인덱스 10)부터 차례대로 비교 (역순 탐색)
            for i in range(10, -1, -1):
                if current_arrow[i] > max_score_arrows[i]:
                    max_score_arrows = current_arrow[:]
                    break
                elif current_arrow[i] < max_score_arrows[i]:
                    break
    
    return max_score_arrows