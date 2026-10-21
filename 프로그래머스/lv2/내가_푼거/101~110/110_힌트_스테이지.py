def solution(cost, hint):
    n = len(cost)
    
    # DP 테이블: { 인벤토리 상태 튜플: 해당 상태에 도달하는 최소 비용 }
    # 초기 상태: 0번 스테이지 시작 전, 모든 힌트권 개수는 0개
    dp = {tuple([0] * n): 0}
    
    for stage in range(n):
        next_dp = {}
        
        for inv, current_cost in dp.items():
            # 1. 현재 스테이지에서 사용할 수 있는 힌트 개수 (최대 n-1개 제한)
            current_hints = inv[stage]
            max_use = min(current_hints, n - 1)
            base_cost = cost[stage][max_use]
            
            # 현재 스테이지를 클리어했으므로 현재 스테이지 힌트권은 모두 소모됨 (0개로 초기화)
            new_inv = list(inv)
            new_inv[stage] = 0
            
            # 선택 1: 힌트 번들을 구매하지 않고 다음으로 진행
            state1 = tuple(new_inv)
            cost1 = current_cost + base_cost
            if state1 not in next_dp or cost1 < next_dp[state1]:
                next_dp[state1] = cost1
            
            # 선택 2: 마지막 스테이지가 아니라면 힌트 번들을 구매하고 진행
            if stage < n - 1:
                bundle_cost = hint[stage][0]
                bundle_tickets = hint[stage][1:]
                
                bought_inv = list(new_inv)
                for t in bundle_tickets:
                    idx = t - 1
                    # 힌트권 개수는 최대 n-1개까지만 의미가 있으므로 상한선 설정
                    bought_inv[idx] = min(n - 1, bought_inv[idx] + 1)
                
                state2 = tuple(bought_inv)
                cost2 = current_cost + base_cost + bundle_cost
                if state2 not in next_dp or cost2 < next_dp[state2]:
                    next_dp[state2] = cost2
                    
        # 다음 스테이지의 DP 테이블로 갱신
        dp = next_dp

    # 모든 스테이지를 완료한 시점의 최소 비용 반환
    return dp[tuple([0] * n)]

print(solution([[160, 140, 120, 110, 60], [290, 270, 260, 120, 10], [160, 130, 120, 60, 20], [160, 120, 80, 70, 20], [110, 70, 60, 30, 20]], [[40, 2, 3], [40, 5, 3], [20, 5, 4], [50, 5, 5]]))