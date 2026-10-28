import heapq

def solution(jobs):
    # 1. 요청 시각순으로 오름차순 정렬
    jobs.sort(key=lambda x: x[0])
    n = len(jobs)
    
    current_time = 0
    total_turnaround_time = 0
    i = 0
    heap = []
    
    # 모든 작업을 처리할 때까지 반복
    while i < n or heap:
        # 1) 현재 시각(current_time) 이하에 요청된 모든 작업을 힙에 투입
        while i < n and jobs[i][0] <= current_time:
            # 우선순위: 소요시간(x[1])이 짧은 것, 요청 시각(x[0])이 빠른 순서
            heapq.heappush(heap, (jobs[i][1], jobs[i][0]))
            i += 1
            
        # 2) 힙에 처리할 작업이 있다면? 가장 우선순위 높은 작업 실행
        if heap:
            req_time, start_time = heapq.heappop(heap)
            current_time += req_time  # 작업이 끝난 시점으로 시간 점프!
            total_turnaround_time += (current_time - start_time) # 반환 시간 누적
        else:
            # 3) 힙이 비어있다면? CPU가 놀고 있으므로 다음 작업이 오는 시각으로 시간 점프!
            current_time = jobs[i][0]
            
    return total_turnaround_time // n