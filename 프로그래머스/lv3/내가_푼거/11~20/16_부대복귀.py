from collections import deque

def solution(n, roads, sources, destination):
    graph = {i : [] for i in range(n + 1)}
    region = [-1] * (n + 1)
    region[destination] = 0

    for x, y in roads :
        graph[x].append(y)
        graph[y].append(x)

    dq = deque([destination])
    visited = {destination}

    while dq :
        cur = dq.popleft()
        require = region[cur] + 1
        for i in graph[cur] :
            if i not in visited :
                region[i] = require
                visited.add(i)
                dq.append(i)

    return [region[i] for i in sources]

print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))