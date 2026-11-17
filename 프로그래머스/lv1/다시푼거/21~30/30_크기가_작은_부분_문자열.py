def solution(t, p):
    n = len(t)
    m = len(p)
        
    return sum(1 for i in range(n - m + 1) if int(t[i : i + m]) <= int(p))