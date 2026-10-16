import math

def solution(k, d):
    possible = 0
    d_sq = d ** 2

    for x in range(0, d + 1, k):
        # 실수 제곱근(** 0.5)과 int() 대신 정수 제곱근 함수 사용
        y_max = math.isqrt(d_sq - x ** 2)
        possible += (y_max // k) + 1

    return possible