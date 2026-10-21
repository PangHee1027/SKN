def solution(triangle):
    n = len(triangle)
    dp = [[triangle[i][j] for j in range(len(triangle[i]))] for i in range(n)]

    for i in range(n - 1) :
        next_len = len(triangle[i + 1])
        for j in range(next_len) :
            if 0 < j < next_len - 1 :
                prev = max(dp[i][j], dp[i][j - 1])
            elif j == 0 :
                prev = dp[i][j]
            elif j == next_len - 1 :
                prev = dp[i][j - 1]
            dp[i + 1][j] += prev

    return max(dp[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))