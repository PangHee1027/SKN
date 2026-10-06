from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    
    dq = deque([(x, 0)])
    visited = {x}
    
    while dq:
        current, count = dq.popleft()
        
        for nxt in (current + n, current * 2, current * 3):
            if nxt == y:
                return count + 1
            
            if nxt < y and nxt not in visited:
                visited.add(nxt)
                dq.append((nxt, count + 1))
                
    return -1