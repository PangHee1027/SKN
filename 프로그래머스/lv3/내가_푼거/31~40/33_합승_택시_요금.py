def solution(n, s, a, b, fares) :
    road = [[0] * (n + 1) for _ in range(n + 1)]
    s2x = [float('inf')] * (n + 1)
    a2x = [float('inf')] * (n + 1)
    b2x = [float('inf')] * (n + 1)
    s2x[s], a2x[a], b2x[b] = 0, 0, 0
    
    def dijkstra(start, distance, visited) :
        def get_smallest_node() :
            min_val = float('inf')
            idx = 0
            for i in range(1, n + 1) :
                if distance[i] and distance[i] < min_val and not visited[i] :
                    min_val = distance[i]
                    idx = i
            return idx
        
        visited[start] = True
        for i in range(1, n + 1) :
            cost = road[start][i]
            if cost :
                distance[i] = cost
        for i in range(n - 1) :
            cur = get_smallest_node()
            visited[cur] = True
            for j in range(1, n + 1) :
                cost = road[cur][j]
                if cost and distance[cur] + cost < distance[j] :
                    distance[j] = distance[cur] + cost
        return distance

    for node1, node2, cost in fares :
        road[node1][node2] = cost
        road[node2][node1] = cost

    a2x, b2x, s2x = [dijkstra(start, dist, [False] * (n + 1)) for start, dist in zip((a, b, s), (a2x, b2x, s2x))]

    min_cost = float('inf')

    for i in range(1, n + 1) :
        min_cost = min(min_cost, a2x[i] + b2x[i] + s2x[i])

    return min_cost

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))