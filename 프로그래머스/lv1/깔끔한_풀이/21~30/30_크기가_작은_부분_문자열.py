def solution(t, p):
    p_len = len(p)
    target = int(p)  # 루프 외부에서 한 번만 형변환
    answer = 0

    for i in range(len(t) - p_len + 1):
        if int(t[i : i + p_len]) <= target:
            answer += 1

    return answer