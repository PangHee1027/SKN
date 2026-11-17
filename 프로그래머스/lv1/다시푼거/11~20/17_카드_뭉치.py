from collections import deque

def solution(cards1, cards2, goal) :
    dq1 = deque(cards1)
    dq2 = deque(cards2)
    for word in goal :
        if dq1 and word == dq1[0] :
            dq1.popleft()
        elif dq2 and word == dq2[0] :
            dq2.popleft()
        else :
            return 'No'
    return 'Yes'