from collections import deque

def solution(queue1, queue2) :
    dq1, dq2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    n = len(queue1) + len(queue2)
    
    if (sum1 + sum2) % 2 :
        return -1
    
    for i in range(2 * n + 1) :
        if sum1 < sum2 :
            dq1.append(dq2.popleft())
            sum1 += dq1[-1]
            sum2 -= dq1[-1]
        elif sum1 > sum2 :
            dq2.append(dq1.popleft())
            sum2 += dq2[-1]
            sum1 -= dq2[-1]
        else :
            return i
        
    return -1