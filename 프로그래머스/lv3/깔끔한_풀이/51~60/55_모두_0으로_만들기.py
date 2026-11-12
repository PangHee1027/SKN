import sys

# 정점의 최대 개수가 30만 개이므로 재귀 깊이 제한을 넉넉히 설정합니다.
sys.setrecursionlimit(1000000)


def solution(a, edges):
    # 전체 가중치의 합이 0이 아니면 모든 정점을 0으로 만드는 것이 불가능합니다.
    if sum(a):
        return -1

    n = len(a)
    graph = [[] for _ in range(n)]
    for n1, n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)

    visited = [False] * n
    total_cost = 0

    def dfs(parent, node):
        nonlocal total_cost
        visited[node] = True

        for nxt_node in graph[node]:
            if not visited[nxt_node]:
                dfs(node, nxt_node)

        # 리프 노드부터 자신의 가중치를 부모에게 넘겨줍니다.
        count = a[node]
        total_cost += abs(count)
        a[node] -= count
        a[parent] += count

    # 0번 노드를 루트로 삼아 DFS 탐색을 시작합니다.
    dfs(0, 0)

    # 루트 노드까지 포함하여 모든 정점의 가중치가 0이 되었는지 확인합니다.
    if any(a):
        return -1

    return total_cost