def solution(s):
    n = len(s)
    i = n // 2
    return s[i] if n % 2 else s[i - 1 : i + 1]