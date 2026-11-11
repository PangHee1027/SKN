def solution(matrix_sizes):
    n = len(matrix_sizes)

    dp = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0

    for i in range(2, n + 1):
        for j in range(n - i + 1):
            start = j
            end = j + i - 1
            cost = float('inf')
            for k in range(j, j + i - 1):
                cost = min(
                    cost,
                    dp[start][k]
                    + dp[k + 1][end]
                    + (
                        matrix_sizes[start][0]
                        * matrix_sizes[k][1]
                        * matrix_sizes[end][1]
                    ),
                )
            dp[start][end] = cost

    return dp[0][-1]