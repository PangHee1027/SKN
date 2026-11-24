from collections import deque

def solution(priorities, location) :
    dq = deque([(x, i) for i, x in enumerate(priorities)])
    answer = 1
    
    while dq :
        cur = dq.popleft()
        if dq and cur[0] < max(dq)[0] :
            dq.append(cur)
            continue
        if cur[1] == location :
            return answer
        else :
            answer += 1
