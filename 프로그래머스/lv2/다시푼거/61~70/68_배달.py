import heapq

def solution(N, road, K) :
    cost = [float('inf')] * (N + 1)
    cost[1] = 0
    graph = {i : [] for i in range(1, N + 1)}
    
    for v1, v2, c in road :
        graph[v1].append((v2, c))
        graph[v2].append((v1, c))
    
    heap = []
    
    for v, c in graph[1] :
        heapq.heappush(heap, (c, 1, v))
    
    while heap :
        c, cur, nxt = heapq.heappop(heap)
        nxt_cost = cost[cur] + c
        if cost[nxt] > nxt_cost :
            cost[nxt] = nxt_cost
            for v, nc in graph[nxt] :
                heapq.heappush(heap, (nc, nxt, v))
                
    return sum(1 for x in cost if x <= K)