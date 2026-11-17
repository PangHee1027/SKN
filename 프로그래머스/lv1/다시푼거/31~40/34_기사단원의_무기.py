def solution(number, limit, power):
    dp = [0] * (number + 1)
    for i in range(1, number + 1) :
        for j in range(i, number + 1, i) :
            dp[j] += 1
        if dp[i] > limit :
            dp[i] = power

    return sum(dp)