def solution(n):
    x = n ** 0.5
    return int(x + 1) ** 2 if x.is_integer() else -1