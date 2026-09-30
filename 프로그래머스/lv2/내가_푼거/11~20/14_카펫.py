def solution(brown, yellow):
    extent = brown + yellow
    answer = []
    for n in range(1, int(extent ** 0.5) + 1) :
        if extent % n == 0 :
            if 2 * (extent // n) + 2 * n == brown  + 4:
                answer = [extent // n, n]
    return sorted(answer, reverse=True)

print(solution(24, 24))