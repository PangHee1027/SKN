import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    idx = 0
    is_deleted = set()

    for op in operations :
        command, num = op.split()
        num = int(num)
        
        if command == "I" :
            heapq.heappush(min_heap, (num, idx))
            heapq.heappush(max_heap, (-num, idx))
            idx += 1
        else :
            # 1이면 최댓값 삭제(max_heap), -1이면 최솟값 삭제(min_heap)
            target_heap = max_heap if num == 1 else min_heap
            
            while target_heap :
                _, i = heapq.heappop(target_heap)
                if i not in is_deleted :
                    break
            else : 
                continue
            is_deleted.add(i)

    # 최종 결과 반환 전 쓰레기 값 청소
    while max_heap and max_heap[0][1] in is_deleted:
        heapq.heappop(max_heap)

    while min_heap and min_heap[0][1] in is_deleted:
        heapq.heappop(min_heap)

    if not min_heap or not max_heap:
        return [0, 0]
    
    return [-max_heap[0][0], min_heap[0][0]]