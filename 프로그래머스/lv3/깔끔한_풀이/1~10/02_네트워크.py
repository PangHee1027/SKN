import sys

sys.setrecursionlimit(1000000)

def solution(n, computers):
    visited = [False] * n
    answer = 0

    def dfs(node):
        visited[node] = True
        for next_node in range(n):
            # 연결되어 있고(computers[node][next_node] == 1), 아직 방문하지 않았다면
            if computers[node][next_node] == 1 and not visited[next_node]:
                dfs(next_node)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1  # 새로운 네트워크 발견

    return answer