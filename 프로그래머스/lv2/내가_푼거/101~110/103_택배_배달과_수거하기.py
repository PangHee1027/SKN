def solution(cap, n, deliveries, pickups):
    distance = 0
    delivery_remain = 0
    pickup_remain = 0
    
    for i in range(n - 1, -1, -1):
        delivery_remain += deliveries[i]
        pickup_remain += pickups[i]

        while delivery_remain > 0 or pickup_remain > 0:
            delivery_remain -= cap
            pickup_remain -= cap
            distance += (i + 1) * 2
            
    return distance

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])) # 16
#print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0])) # 30