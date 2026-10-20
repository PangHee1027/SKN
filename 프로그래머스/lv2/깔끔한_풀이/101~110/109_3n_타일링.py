def solution(n):
    # 홀수 길이는 타일로 채울 수 없으므로 0 반환
    if n % 2:
        return 0
    if n == 2:
        return 3

    # a는 f(n-4) 역할, b는 f(n-2) 역할을 담당합니다.
    a, b = 1, 3
    m = n // 2

    # n이 6부터 시작하는 경우에 맞춰 루프를 순회합니다.
    for _ in range(3, m + 1):
        # 4 * (직전 값 b) - (전전 값 a) 로 다음 값을 갱신합니다.
        a, b = b, (4 * b - a) % 1000000007
    
    return b