def solution(n, s, a, b, fares):
    # 1. 거리 테이블을 충분히 큰 값(무한대)으로 초기화
    dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dist[i][i] = 0  # 자기 자신으로 가는 비용은 0
        
    # 2. 주어진 요금 정보를 양방향 간선으로 테이블에 반영
    for u, v, cost in fares:
        dist[u][v] = cost
        dist[v][u] = cost
        
    # 3. 플로이드-워샬 알고리즘: k번 노드를 거쳐가는 모든 최단 거리 갱신
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    # 4. 모든 지점 i를 '합승을 마치고 헤어지는 지점'으로 가정하여 최소 비용 탐색
    min_cost = float('inf')
    for i in range(1, n + 1):
        # (출발지 s -> 지점 i) + (지점 i -> A의 도착지 a) + (지점 i -> B의 도착지 b)
        cost_sum = dist[s][i] + dist[i][a] + dist[i][b]
        min_cost = min(min_cost, cost_sum)
        
    return min_cost