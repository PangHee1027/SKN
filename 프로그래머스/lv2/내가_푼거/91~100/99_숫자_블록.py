import math

def max_divisor(num) :
    qrt_num = math.isqrt(num)
    min_divisor = 0
    max_divisor = 0
    if num == 1 :
        return 0
    for i in range(2, qrt_num + 1) :
        if not num % i :
            min_divisor = i
            max_divisor = num // min_divisor
            if max_divisor <= 10000000 :
                break
    else :
        max_divisor = min_divisor
    if min_divisor :
        return max_divisor
    return 1

def solution(begin, end):
    answer = []

    for i in range(begin, end + 1) :
        answer.append(max_divisor(i))

    return answer

print(solution(12, 49))