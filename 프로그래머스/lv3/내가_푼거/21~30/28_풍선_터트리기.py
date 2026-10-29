import heapq

def solution(a) :
    n = len(a)
    if n < 3 :
        return n
    heap = a[2:]
    visited = {a[0]}
    left_min = a[0]
    possible = 2
    heapq.heapify(heap)

    for num in a[1:-1] :
        visited.add(num)
        while heap[0] in visited :
            heapq.heappop(heap)
        if num < left_min :
            possible += 1
            left_min = num
            continue
        if num < heap[0] :
            possible += 1
            continue
        
    return possible

print(solution([9, -1, -5]))
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))