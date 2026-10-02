import heapq

def solution(scoville, K):
    heap = []
    for s in scoville :
        heapq.heappush(heap, s)
    count = 0
    while True :
        if heap[0] >= K :
            return count
        if len(heap) == 1 :
            return -1
        
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)

        heapq.heappush(heap, first + second * 2)
        count += 1
        

print(solution([1, 2, 3, 9, 10, 12], 7))