import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)
    idx = 0
    is_deleted = set()

    for op in operations :
        op, num = op.split()
        num = int(num)
        if op[0] == "I" :
            heapq.heappush(min_heap, (num, idx))
            heapq.heappush(max_heap, (-num, idx))
            idx += 1
        else :
            if num == 1 :
                while max_heap :
                    _, i = heapq.heappop(max_heap)
                    if i not in is_deleted :
                        break
                else : 
                    continue
                is_deleted.add(i)
            else :
                while min_heap :
                    _, i = heapq.heappop(min_heap)
                    if i not in is_deleted :
                        break
                else : 
                    continue
                is_deleted.add(i)

    while max_heap and max_heap[0][1] in is_deleted:
        heapq.heappop(max_heap)

    while min_heap and min_heap[0][1] in is_deleted:
        heapq.heappop(min_heap)

    if not min_heap or not max_heap:
        return [0, 0]
    
    return [-max_heap[0][0], min_heap[0][0]]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))