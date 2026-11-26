from collections import deque

def solution(bridge_length, weight, truck_weights) :
    sum_weight = 0
    bridge_dq = deque([0] * bridge_length, maxlen = bridge_length)
    truck_dq = deque(truck_weights)
    answer = 0
    while sum_weight or truck_dq :
        answer += 1
        sum_weight -= bridge_dq.popleft()
        if truck_dq and sum_weight + truck_dq[0] <= weight :
            bridge_dq.append(truck_dq.popleft())
            sum_weight += bridge_dq[-1]
        else :
            bridge_dq.append(0)
            
    return answer