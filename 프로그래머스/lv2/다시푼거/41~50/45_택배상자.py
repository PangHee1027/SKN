from collections import deque

def solution(order):
    n = len(order)
    dq = deque(range(1, n + 1))
    stack = []
    answer = 0
    
    for target in order :
        while dq and target >= dq[0] :
            stack.append(dq.popleft())
        if stack and stack[-1] == target :
            stack.pop()
            answer += 1
        else :
            break
        
    return answer