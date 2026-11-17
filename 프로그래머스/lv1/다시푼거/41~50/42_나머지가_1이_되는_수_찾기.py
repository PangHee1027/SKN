from math import isqrt

def solution(n):
    qrt_n = isqrt(n - 1)
    for i in range(2, qrt_n + 1) :
        if not (n - 1) % i :
            return i
    return n - 1