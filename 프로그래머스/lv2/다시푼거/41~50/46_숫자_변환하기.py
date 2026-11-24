from collections import deque

def solution(x, y, n) :
    visited = {x}
    dq = deque([(x, 0)]) 
    
    while dq :
        cur, cost = dq.popleft()
        multi_2 = cur * 2
        multi_3 = cur * 3
        plus_n = cur + n
        
        if cur == y :
            return cost
        
        if multi_2 not in visited and multi_2 <= y :
            dq.append((multi_2, cost + 1))
            visited.add(multi_2)
        if multi_3 not in visited and multi_3 <= y :
            dq.append((multi_3, cost + 1))
            visited.add(multi_3)
        if plus_n not in visited and plus_n <= y :
            dq.append((plus_n, cost + 1))
            visited.add(plus_n)

    return -1