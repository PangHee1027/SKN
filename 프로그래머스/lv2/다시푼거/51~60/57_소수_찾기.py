from math import isqrt
from itertools import permutations

def is_prime(n) :
    if n == 1 or n == 0 :
        return False
    qrt_n = isqrt(n)
    for i in range(2, qrt_n + 1) :
        if not n % i :
            return False
    return True

def solution(numbers):
    numbers = list(numbers)
    n = len(numbers)
    result = set()
    
    for i in range(1, n + 1) :
        for permutation in permutations(numbers, i) :
            num = int(''.join(permutation))
            if is_prime(num) :
                result.add(num)
    
    print(result)
    return len(result)