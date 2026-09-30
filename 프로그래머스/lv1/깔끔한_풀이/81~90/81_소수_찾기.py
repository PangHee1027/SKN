def solution(n):
    # 0부터 n까지 True로 초기화 (0과 1은 소수가 아니므로 False)
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    # 2부터 sqrt(n)까지 순회하며 배수들 제거
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            # i의 배수들을 False로 처리 (i*i 이전은 이미 처리됨)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
                
    return sum(is_prime)