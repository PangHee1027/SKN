def solution(n, lost, reserve):
    # 1. 여벌이 있지만 도난당한 학생은 본인이 입어야 하므로 양쪽에서 모두 제거
    real_reserve = set(reserve) - set(lost)
    real_lost = set(lost) - set(reserve)

    # 2. 여벌이 있는 학생 기준으로 앞번호 -> 뒷번호 순으로 빌려줌 (그리디)
    for r in sorted(real_reserve):
        if r - 1 in real_lost:
            real_lost.remove(r - 1)
        elif r + 1 in real_lost:
            real_lost.remove(r + 1)

    # 3. 전체 학생 수 - 끝까지 체육복이 없는 학생 수
    return n - len(real_lost)