def solution(n):
    if n % 2 :
        return 0
    if n == 2 :
        return 3

    a, b = 1, 3
    m = n // 2

    for _ in range(2, m + 1) :
        a, b = b, (4 * b - a) % 1000000007
    
    return b