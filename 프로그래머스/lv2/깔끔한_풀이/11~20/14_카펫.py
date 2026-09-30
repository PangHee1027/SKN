def solution(brown, yellow):
    total = brown + yellow
    for h in range(1, int(total ** 0.5) + 1):
        if total % h == 0:
            w = total // h
            if 2 * w + 2 * h == brown + 4:
                return [w, h]  # w >= h 가 보장되므로 즉시 반환