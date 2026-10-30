# 방법 1 : 플로이드 워샬 (N < 1000)
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

# 방법 2 : 다익스트라 개선
import heapq

def solution(n, s, a, b, fares):
    # 1. 인접 리스트(Adjacency List) 방식으로 그래프 구성
    graph = [[] for _ in range(n + 1)]
    for u, v, cost in fares:
        graph[u].append((v, cost))
        graph[v].append((u, cost))

    # 2. 다익스트라 함수 (최소 힙 활용)
    def dijkstra(start):
        distance = [float('inf')] * (n + 1)
        distance[start] = 0
        q = []
        # 힙에 (누적 비용, 현재 노드 번호) 형태로 삽입
        heapq.heappush(q, (0, start))

        while q:
            dist, now = heapq.heappop(q)

            # 이미 처리된 적 있는 노드이고, 현재 기록된 최단 거리보다 크면 무시
            if distance[now] < dist:
                continue

            # 현재 노드와 인접한 노드들 확인
            for next_node, next_cost in graph[now]:
                cost = dist + next_cost
                # 더 짧은 경로를 발견한 경우에만 갱신 후 힙에 삽입
                if cost < distance[next_node]:
                    distance[next_node] = cost
                    heapq.heappush(q, (cost, next_node))

        return distance

    # 3. 출발지 s, a, b 각각에 대해 최단 거리 테이블 계산
    a2x, b2x, s2x = [dijkstra(start) for start in (a, b, s)]

    # 4. 모든 정점 i를 '합승을 마치고 헤어지는 중간 지점'으로 가정하여 최소 비용 탐색
    min_cost = float('inf')
    for i in range(1, n + 1):
        min_cost = min(min_cost, s2x[i] + a2x[i] + b2x[i])

    return min_cost