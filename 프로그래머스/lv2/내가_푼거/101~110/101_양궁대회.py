from itertools import combinations_with_replacement

def solution(n, info):
    max_score_arrows = [-1]
    max_score = 0
    for case in combinations_with_replacement(range(11), n) :
        current_arrow = [0] * 11
        current_info = [-x for x in info]
        for i in case :
            current_info[(10-i)] += 1
            current_arrow[(10-i)] += 1
        score = 0
        for i, count in enumerate(current_info) :
            if count > 0 :
                score += 10 - i
            elif count < 0 :
                score -= 10 - i
            else :
                if info[i] :
                    score -= 10 - i

        if score > max_score :
            max_score_arrows = current_arrow
            max_score = score
        elif score > 0 and score == max_score :
            for i in range(10, -1, -1):
                if current_arrow[i] > max_score_arrows[i]:
                    max_score_arrows = current_arrow
                    break
                elif current_arrow[i] < max_score_arrows[i]:
                    break
    
    return max_score_arrows