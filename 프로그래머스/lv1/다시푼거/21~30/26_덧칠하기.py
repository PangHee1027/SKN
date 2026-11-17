from collections import deque

def solution(n, m, section):
    dq = deque(section)
    answer = 0
    
    while dq :
        nxt = dq.popleft()
        coverage = nxt + m
        while dq and dq[0] < coverage :
            dq.popleft()
        answer += 1       
        
    return answer