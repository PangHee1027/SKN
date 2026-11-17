def solution(left, right) :
    dp = [0] * (right + 1)
    for i in range(1, right + 1) :
        for j in range(i, right + 1) :
            if not j % i  :
                dp[j] += 1
                
    return sum(-i if dp[i] % 2 else i for i in range(left, right + 1))