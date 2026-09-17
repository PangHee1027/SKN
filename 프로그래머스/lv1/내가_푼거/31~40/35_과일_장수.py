def solution(k, m, score):
    score.sort(reverse = True)
    answer = 0
    for i in range(0, len(score), m) :
        answer += (min(score[i:i + m]) * m) if i + m <= len(score) else 0
    return answer

# print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))