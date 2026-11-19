from math import isqrt

def solution(brown, yellow) :
    n = brown + yellow
    qrt_n = isqrt(n)
    
    for i in range(1, qrt_n + 1) :
        if not n % i :
            j = n // i
            if (i - 2) * (j - 2) == yellow :
                return [j, i]