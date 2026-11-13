import sys
sys.setrecursionlimit(1000000)

def solution(n, lighthouse):
    # 1. 딕셔너리 대신 리스트 기반 인접 리스트 선언 (속도 향상)
    graph = [[] for _ in range(n + 1)]
    for n1, n2 in lighthouse:
        graph[n1].append(n2)
        graph[n2].append(n1)
    
    dp = [[0] * 2 for _ in range(n + 1)]

    # 2. visited 배열 대신 parent 인자를 활용해 역주행 방지
    def dfs(node, parent):
        for nxt in graph[node]:
            if nxt == parent:
                continue
            dfs(nxt, node)
            dp[node][0] += dp[nxt][1]
            dp[node][1] += min(dp[nxt])
        dp[node][1] += 1

    # 루트 노드(1번)부터 탐색 시작 (부모는 존재하지 않으므로 0 또는 None 전달)
    dfs(1, 0)

    return min(dp[1])