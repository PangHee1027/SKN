from collections import deque

def solution(people, limit):
    people.sort()
    
    dq = deque(people)
    answer = 0
    
    while dq :
        cur = limit
        cur -= dq.pop()
        if dq and dq[0] <= cur :
            dq.popleft()
        answer += 1
        
    return answer