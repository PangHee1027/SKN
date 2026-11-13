import sys
sys.setrecursionlimit(1000000)

def solution(n, lighthouse) :
    def dfs(node) :
        visited[node] = True
        for nxt in graph[node] :
            if visited[nxt] :
                continue
            dfs(nxt)
            dp[node][0] += dp[nxt][1]
            dp[node][1] += min(dp[nxt])
        dp[node][1] += 1
        return
    
    graph = {i + 1 : [] for i in range(n)}
    dp = [[0] * 2 for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for n1, n2 in lighthouse :
        graph[n1].append(n2)
        graph[n2].append(n1)
    
    dfs(1)

    return min(dp[1])

print(solution(8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]))
print(solution(10, [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]))

