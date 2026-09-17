def solution(n, m, section):
    answer = 0
    painted_until = 0  # 롤러로 칠이 완료된 마지막 구역 번호

    for s in section:
        # 현재 구역(s)이 아직 칠해지지 않은 구역이라면
        if s > painted_until:
            answer += 1
            painted_until = s + m - 1  # s부터 m길이만큼 칠함

    return answer