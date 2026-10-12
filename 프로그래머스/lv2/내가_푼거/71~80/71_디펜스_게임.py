import heapq

def solution(n, k, enemy):
    heap = []
    answer = len(enemy)
    heap_sum = 0
    remain = k
    for num in enemy :
        if remain <= 0 and num + heap_sum > n :
            answer = k + len(heap)
            break
        heapq.heappush(heap, -num)
        heap_sum += num
        while heap_sum > n :
            largest = heapq.heappop(heap)
            heap_sum += largest
            remain -= 1

    return answer

print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
print(solution(2, 4, [3, 3, 3, 3]))