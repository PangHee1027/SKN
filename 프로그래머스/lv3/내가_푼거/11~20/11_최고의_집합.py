import heapq

def solution(n, s):
    if n > s :
        return [-1]
    if not s % n :
        return [s // n] * n

    answer = [int(s / n)] * n
    heapq.heapify(answer)
    sum_answer = sum(answer)

    while sum_answer != s :
        heapq.heappush(answer, heapq.heappop(answer) + 1)
        sum_answer += 1

    return sorted(list(answer))

print(solution(2, 9))
print(solution(2, 1))
print(solution(2, 8))