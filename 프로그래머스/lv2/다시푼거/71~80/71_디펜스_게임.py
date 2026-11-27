import heapq

def solution(n, k, enemy):
    heap = []
    len_heap = 0
    
    max_round = len(enemy)
    
    for i, e in enumerate(enemy) :
        heapq.heappush(heap, e)
        len_heap += 1
        if len_heap > k :
            n -= heapq.heappop(heap)
            len_heap -= 1
        if n < 0 :
            return i  
        
    return max_round