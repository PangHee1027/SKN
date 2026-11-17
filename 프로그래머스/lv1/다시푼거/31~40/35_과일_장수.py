def solution(k, m, score) :
    score.sort(reverse = True)
    n = len(score)
    return sum(min(score[i : i + m]) * m for i in range(0, n, m) if len(score[i : i + m]) == m)