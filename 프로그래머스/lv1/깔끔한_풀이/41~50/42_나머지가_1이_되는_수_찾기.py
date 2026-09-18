def solution(n):
    target = n - 1
    # 2부터 sqrt(target)까지만 탐색
    for i in range(2, int(target**0.5) + 1):
        if target % i == 0:
            return i
    # 약수가 없으면 target(즉, n - 1) 자체가 소수이므로 target 반환
    return target