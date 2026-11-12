def solution(n, tops) :
    dp = [[0] * 2 for _ in range(n)]
    MOD = 10007

    dp[0][0] = 1
    dp[0][1] = 3 if tops[0] == 1 else 2

    for i in range(1, n) :
        if not tops[i] :
            dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
            dp[i][1] = (dp[i - 1][0] + 2 * dp[i - 1][1]) % MOD
        else :
            dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
            dp[i][1] = (2 * dp[i - 1][0] + 3 * dp[i - 1][1]) % MOD
    return sum(dp[-1]) % 10007