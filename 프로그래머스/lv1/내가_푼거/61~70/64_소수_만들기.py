import math
from itertools import combinations

def solution(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    def sum_combination(nums, n) :
        result = list(combinations(nums, n))
        for i in range(len(result)) :
            result[i] = sum(result[i])
        return result
    
    answer = 0
    sum_comb = sum_combination(nums, 3)

    for n in sum_comb :
        answer += 1 if is_prime(n) else 0

    return answer

print(solution([1,2,7,6,4]))