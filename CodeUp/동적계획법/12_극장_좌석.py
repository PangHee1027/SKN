n = int(input())
fixed = int(input())
fixed_seat = set()

for _ in range(fixed) :
    fixed_seat.add(int(input()))

dp = [[0] * 2 for _ in range(n + 1)]

dp[1][0], dp[1][1] = 1, 0

for i in range(2, n + 1) :
    if i in fixed_seat or i - 1 in fixed_seat :
        dp[i][0], dp[i][1] = sum(dp[i - 1]), 0
        continue
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
    dp[i][1] = dp[i - 1][0]

print(sum(dp[-1]))
