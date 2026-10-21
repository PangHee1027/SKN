import heapq

def solution(n, works):
    works = [-x for x in works]
    heapq.heapify(works)

    for i in range(n) :
        cur = heapq.heappop(works)
        cur += 1
        if cur :
            heapq.heappush(works, cur)
        if not works :
            return 0

    answer = 0

    for work in works :
        answer += work ** 2
    
    return answer

print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))