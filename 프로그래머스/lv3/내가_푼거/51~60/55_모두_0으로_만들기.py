import sys
sys.setrecursionlimit(1000000)

def solution(a, edges) :
    def dfs(parent, node) :
        visited[node] = True
        result = 0
        for nxt_node in graph[node] :
            if visited[nxt_node] :
                continue
            result += dfs(node, nxt_node)
        count = a[node]
        result += abs(count)
        a[node] -= count
        a[parent] += count

        return result

    if sum(a) :
        return -1

    n = len(a)
    graph = {i : [] for i in range(n)}
    visited = [False] * n
    for n1, n2 in edges :
        graph[n1].append(n2)
        graph[n2].append(n1)

    answer = 0

    for nxt in graph[0] :
        answer += dfs(0, nxt)

    if any(x for x in a) :
        return -1

    return answer

print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]))
print(solution([0,1,0], [[0,1],[1,2]]))