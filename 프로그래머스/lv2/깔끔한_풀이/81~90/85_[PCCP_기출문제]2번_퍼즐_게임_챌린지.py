def solution(diffs, times, limit):
    # 이전 퍼즐 시간을 미리 결합 (첫 번째 퍼즐의 이전 시간은 0)
    times_zip = list(zip(times, [0] + times[:-1]))

    def calc_time(level):
        result = 0
        for d, (time_cur, time_prev) in zip(diffs, times_zip):
            if d <= level:
                result += time_cur
            else:
                # 틀린 횟수 * (현재 시간 + 이전 시간) + 마지막 정답 시간
                result += (d - level) * (time_cur + time_prev) + time_cur
        return result

    a, b = 1, max(diffs)
    answer = b

    while a <= b:
        level = (a + b) // 2
        if calc_time(level) <= limit:
            answer = level # 조건을 만족하면 저장해 두고 더 작은 숙련도 탐색
            b = level - 1
        else:
            a = level + 1

    return answer