from math import isqrt

def solution(n) :
    answer = 0
    qrt_n = isqrt(n)
    for i in range(1, qrt_n + 1) :
        if not n % i :
            if i % 2 :
                answer += 1
            j = n // i
            if j != i and j % 2 :
                answer += 1
    return answer