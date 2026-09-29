def solution(n, m):
    # 유클리드 호제법으로 최대공약수 구하기
    a, b = n, m
    while b > 0:
        a, b = b, a % b
    
    gcd = a
    lcm = (n * m) // gcd
    
    return [gcd, lcm]