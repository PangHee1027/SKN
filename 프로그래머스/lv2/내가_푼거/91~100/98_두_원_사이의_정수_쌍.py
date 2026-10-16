import math

def solution(r1, r2):
    r1_dot, r2_dot = -2, 0

    for i in range(-r1, r1 + 1, 1) :
        max_y = math.isqrt(r1 ** 2 - i ** 2)
        if max_y == (r1 ** 2 - i ** 2) ** 0.5 and -r1 < i < r1 :
            max_y -= 1
        r1_dot += max_y * 2 + 1


    for i in range(-r2, r2 + 1, 1) :
        max_y = math.isqrt(r2 ** 2 - i ** 2)
        r2_dot += max_y * 2 + 1
    answer = 0
    return r2_dot - r1_dot

print(solution(2, 3))