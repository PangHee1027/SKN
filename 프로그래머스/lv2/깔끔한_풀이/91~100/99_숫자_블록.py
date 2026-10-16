import math

def get_max_divisor(num):
    if num == 1:
        return 0
    
    limit = 10_000_000
    
    # 2부터 제곱근까지 탐색 (약수는 쌍으로 존재하므로 작은 수를 기준으로 탐색)
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            max_d = num // i  # 1000만 이하 중 가장 큰 약수 후보
            if max_d <= limit:
                return max_d
                
    # 조건을 만족하는 약수가 없다면 1 리턴 (소수 등)
    return 1

def solution(begin, end):
    # 리스트 컴프리헨션을 사용해 가독성을 높임
    return [get_max_divisor(i) for i in range(begin, end + 1)]