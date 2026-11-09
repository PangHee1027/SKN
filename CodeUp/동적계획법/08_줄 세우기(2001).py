n = int(input())
l = []

for _ in range(n) :
    l.append(int(input()))

dp = [1] * (n)

for i in range(n) :
    for j in range(i) :
        if l[i] > l[j] :
            dp[i] = max(dp[j] + 1, dp[i])

print(n - max(dp))
