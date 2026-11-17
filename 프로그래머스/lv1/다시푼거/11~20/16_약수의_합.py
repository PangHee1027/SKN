from math import isqrt

def solution(n) :
    qrt_n = isqrt(n)
    result = 0
    for i in range(1, qrt_n + 1) :
        if not n % i :
            result += i
            if i < n // i :
                result += n // i
    return result
