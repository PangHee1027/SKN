def solution(n) :
    dp = [0] * (n + 1)
    for i in range(1, n + 1) :
        for j in range(i, n + 1, i) :
            dp[j] += 1
        
    return dp.count(2)