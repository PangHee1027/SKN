import heapq

def solution(numbers) :
    n = len(numbers)
    answer = [-1] * n
    heap = []
    for i in range(n - 1) :
        cur, nxt = numbers[i], numbers[i + 1]
        if nxt > cur :
            answer[i] = nxt
        else :
            heapq.heappush(heap, (cur, i))
        while heap and heap[0][0] < cur :
            _, idx = heapq.heappop(heap)
            answer[idx] = cur
        while heap and heap[0][0] < nxt :
            _, idx = heapq.heappop(heap)
            answer[idx] = nxt
    return answer