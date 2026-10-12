import heapq

def solution(N, road, K):
    answer = 0
    times = [float("inf")] * (N + 1)
    times[1] = 0 

    graph = {i : {} for i in range(N + 1)}
    
    for v1, v2, time in road:
        # 양방향 연결 정보 추가
        graph[v1][v2] = min(graph[v1].get(v2, float("inf")), time)
        graph[v2][v1] = min(graph[v2].get(v1, float("inf")), time)

    hq = []
    heapq.heappush(hq, (0, 1))

    while hq:
        time, vil = heapq.heappop(hq)
        
        # [추가하면 좋은 부분] 이미 더 짧은 경로로 방문한 적이 있다면 무시
        if times[vil] < time:
            continue
            
        for target_vil, duration in graph[vil].items():
            if times[target_vil] > time + duration:
                times[target_vil] = time + duration
                heapq.heappush(hq, (times[target_vil], target_vil))
                
    return sum([1 for x in times if x <= K])