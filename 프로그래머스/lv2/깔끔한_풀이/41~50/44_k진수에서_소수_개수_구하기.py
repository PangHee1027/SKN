def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def convert_base(n, k):
    digits = []
    while n > 0:
        n, remainder = divmod(n, k)
        digits.append(str(remainder))
    return "".join(reversed(digits))

def solution(n, k):
    # 1. k진수로 변환
    k_num_str = convert_base(n, k)
    
    # 2. '0'으로 분할 후 빈 문자열 제거
    candidates = filter(None, k_num_str.split('0'))
    
    # 3. 각 숫자에 대해 소수 여부 판별 후 개수 합산
    return sum(1 for num in candidates if is_prime(int(num)))