from collections import deque

def solution(x, y, n):
    if x == y :
        return 0
    answer = 0
    dq = deque([(x, 0)])
    visited = {x}
    while dq :
        current, count = dq.popleft()
        multi_2 = current * 2
        multi_3 = current * 3
        plus_n = current + n
        if multi_2 == y or multi_3 == y or plus_n == y :
            return count + 1
        if multi_2 < y and multi_2 not in visited :
            dq.append((multi_2, count + 1))
            visited.add(multi_2)
        if multi_3 < y and multi_3 not in visited :
            dq.append((multi_3, count + 1))
            visited.add(multi_3)
        if plus_n < y and plus_n not in visited :
            dq.append((plus_n, count + 1))
            visited.add(plus_n)
    return -1

print(solution(10, 40, 5))
print(solution(10, 40, 30))
print(solution(2, 5, 4))