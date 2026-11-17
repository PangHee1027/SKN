from math import isqrt

def solution(n):
    qrt_n = isqrt(n)
    if qrt_n ** 2 == n :
        return (qrt_n + 1) ** 2
    return -1