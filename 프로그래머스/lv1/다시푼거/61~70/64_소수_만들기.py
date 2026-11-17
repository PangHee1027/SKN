from itertools import combinations
from math import isqrt

def solution(nums) :
    def is_prime(n) :
        qrt_n = isqrt(n)
        for i in range(2, qrt_n + 1) :
            if not n % i :
                return False
        return True
    
    return len([sum(comb) for comb in combinations(nums, 3) if is_prime(sum(comb))])