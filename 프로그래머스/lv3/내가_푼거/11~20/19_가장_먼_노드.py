from collections import deque

def solution(n, edge):
    distance = [-1] * (n + 1)
    distance[1] = 0
    graph = {i : [] for i in range(n + 1)}
    dq = deque([1])

    for node1, node2 in edge :
        graph[node1].append(node2)
        graph[node2].append(node1)

    while dq :
        node = dq.popleft()
        require = distance[node] + 1
        for next_node in graph[node] :
            if distance[next_node] == -1 :
                distance[next_node] = require
                dq.append(next_node)

    return distance.count(max(distance))

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))