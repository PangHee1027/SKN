from collections import deque

def solution(targets):
    targets.sort(key = lambda x : x[1])
    stack = []
    dq = deque(targets)

    while dq :
        current = dq.popleft()
        if not stack :
            stack.append(current)
            continue
        pre = stack[-1]
        if  current[0] < pre[1] :
            pre = [current[0], pre[1]]
            stack[-1] = pre
        else :
            stack.append(current)

    return len(stack)

print(solution([[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]))