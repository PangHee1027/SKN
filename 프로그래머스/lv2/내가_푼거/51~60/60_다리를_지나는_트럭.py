from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    current_weight = 0
    
    while bridge:
        time += 1

        pass_truck = bridge.popleft()
        current_weight -= pass_truck
        
        if trucks:
            if current_weight + trucks[0] <= weight:
                cur_truck = trucks.popleft()
                current_weight += cur_truck
                bridge.append(cur_truck)
            else:
                bridge.append(0)
                
    return time

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))