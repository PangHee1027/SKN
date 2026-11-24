import heapq

def solution(prices) :
    n = len(prices)
    heap, answer = [], [0] * n
    
    for i, x in enumerate(prices) :
        heapq.heappush(heap, (-x, i))
        while heap and -heap[0][0] > x :
            _, idx = heapq.heappop(heap)
            answer[idx] = i - idx
    while heap :
        _, idx = heapq.heappop(heap)
        answer[idx] = n - idx - 1
        
    return answer