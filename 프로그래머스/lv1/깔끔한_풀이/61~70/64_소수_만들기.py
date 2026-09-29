from itertools import combinations

def solution(nums):
    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # is_prime() 결과(True=1, False=0)를 바로 더함
    return sum(is_prime(sum(c)) for c in combinations(nums, 3))