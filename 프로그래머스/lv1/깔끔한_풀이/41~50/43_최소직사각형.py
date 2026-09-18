def solution(sizes):
    max_w = 0
    max_h = 0

    for w, h in sizes:
        # 두 변 중 큰 값을 max_w, 작은 값을 max_h 그룹으로 보냄
        max_w = max(max_w, max(w, h))
        max_h = max(max_h, min(w, h))

    return max_w * max_h