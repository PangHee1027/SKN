from itertools import permutations

def is_prime(n):
    """소수 여부를 판별하는 보조 함수"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    # 1. 모든 숫자 조합을 생성하여 int로 변환 및 중복 제거
    created_numbers = {
        int("".join(p))
        for i in range(1, len(numbers) + 1)
        for p in permutations(numbers, i)
    }
    
    # 2. 소수 조건에 맞는 숫자의 개수만 카운트
    return sum(1 for num in created_numbers if is_prime(num))