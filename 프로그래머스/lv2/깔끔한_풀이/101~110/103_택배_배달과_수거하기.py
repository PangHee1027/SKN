import math

def solution(cap, n, deliveries, pickups):
    distance = 0
    
    # 1. 뒤에서부터(가장 먼 집부터) 처리해야 할 남은 물량을 추적할 변수 초기화
    delivery_remain = 0
    pickup_remain = 0
    
    # 2. 가장 먼 집(인덱스 n-1)부터 집 0번(인덱스 0)까지 역순으로 탐색합니다.
    for i in range(n - 1, -1, -1):
        # 이번 집에서 발생한 배달/수거 물량을 누적합니다.
        # (이전 집들을 돌면서 처리하지 못하고 밀려온 미처리 물량이 합산됩니다)
        delivery_remain += deliveries[i]
        pickup_remain += pickups[i]

        # 3. 이번 집(i+1번째 집)이나 그보다 더 먼 곳에 
        #    배달 또는 수거해야 할 물량이 남아있는 경우에만 트럭을 보냅니다.
        if delivery_remain > 0 or pickup_remain > 0:
            
            # 4. 트럭의 최대 용량(cap)으로 현재 남은 물량을 모두 처리하려면 
            #    이 거리(i + 1)까지 최소 몇 번 왕복해야 하는지 계산합니다.
            # - 배달 기준 필요한 왕복 횟수와 수거 기준 필요한 왕복 횟수 중 
            #   더 많이 필요한(큰) 횟수를 전체 왕복 횟수(cnt)로 채택합니다.
            cnt = max(
                math.ceil(delivery_remain / cap),
                math.ceil(pickup_remain / cap)
            )
            
            # 5. 총 이동 거리 누적: (왕복 거리: (i + 1) * 2) * (왕복 횟수: cnt)
            distance += (i + 1) * 2 * cnt
            
            # 6. 이번 왕복(cnt번) 동안 트럭이 처리한 만큼 
            #    남은 배달 및 수거 물량을 각각 차감해 줍니다.
            delivery_remain -= cap * cnt
            pickup_remain -= cap * cnt
            
    return distance