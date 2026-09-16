def solution(a, b, g, s, w, t):
    start = 1
    # 최대 시간: (최대 금+은 수량 2*10^9) * (최대 편도 시간 10^5 * 2) / (최소 용량 1)
    end = 4 * 10**14
    answer = end

    while start <= end:
        mid = (start + end) // 2

        total_g = 0
        total_s = 0
        total_max = 0

        for i in range(len(g)):
            # mid 시간 동안 i번 도시 트럭이 운반할 수 있는 횟수 (편도 출발 기준)
            moves = (mid + t[i]) // (t[i] * 2)
            max_carry = moves * w[i]

            total_g += min(g[i], max_carry)
            total_s += min(s[i], max_carry)
            total_max += min(g[i] + s[i], max_carry)

        # 조건을 만족하면 시간을 줄여서 다시 탐색
        if total_g >= a and total_s >= b and total_max >= (a + b):
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer