def solution(n: int, money: list[int]) -> int:
    # 1. 작은 동전부터 차례대로 조합할 수 있도록 오름차순 정렬
    money.sort()
    
    # 2. dp[i] : i원을 거슬러 주는 방법의 수
    dp = [0] * (n + 1)
    dp[0] = 1  # 0원을 만드는 방법은 아무것도 안 쓰는 1가지
    
    # 3. 동전을 하나씩 누적하며 경우의 수 계산
    for m in money:
        for i in range(m, n + 1):
            dp[i] = (dp[i] + dp[i - m]) % 1000000007
            
    return dp[n]