n = int(input())
coins = list(map(int, input().split()))

if n < 3 :
    print(sum(coins))
else :
    dp = [0] * n
    dp[0] = coins[0]
    dp[1] = coins[0] + coins[1]
    dp[2] = max(coins[0] + coins[1], coins[0] + coins[2], coins[1] + coins[2])

    for i in range(3, n) :
        dp[i] = max(dp[i - 1], dp[i - 2] + coins[i], coins[i - 1] + coins[i] + dp[i - 3])

    print(dp[-1])

