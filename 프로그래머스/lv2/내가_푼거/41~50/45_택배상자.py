from collections import deque

def solution(order):
    answer = 0
    dq = deque(range(1, len(order) + 1))
    order = deque(order)
    stack = []

    for _ in range(len(order)) :
        hope = order.popleft()
        if not dq and stack and stack[-1] != hope :
            break
        if stack and stack[-1] == hope :
            stack.pop()
            answer += 1
            continue
        while dq and dq[0] != hope :
            stack.append(dq.popleft())
        if dq :
            dq.popleft()
            answer += 1

    return answer

print(solution([4, 3, 1, 2, 5]))