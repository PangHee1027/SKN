def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0

    # m개씩 끊었을 때 상자 내 최하점 사과 위치는 m-1, 2m-1, 3m-1...
    for i in range(m - 1, len(score), m):
        answer += score[i] * m

    return answer