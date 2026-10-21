from functools import lru_cache

def solution(cost, hint):
    n = len(cost)
    
    @lru_cache(None)
    def dfs(stage, inv):
        # 모든 스테이지를 완료한 경우 비용 0 반환
        if stage == n:
            return 0
        
        # 현재 스테이지에서 사용할 수 있는 힌트 개수 (최대 n-1개 제한)
        current_hints = inv[stage]
        max_use = min(current_hints, n - 1)
        base_cost = cost[stage][max_use]
        
        # 현재 스테이지를 클리어했으므로 현재 스테이지 힌트권은 소모됨 (0개로 초기화)
        new_inv = list(inv)
        new_inv[stage] = 0
        
        # 선택 1: 힌트 번들을 구매하지 않고 다음 스테이지로 진행
        min_cost = base_cost + dfs(stage + 1, tuple(new_inv))
        
        # 선택 2: 마지막 스테이지가 아니라면 힌트 번들을 구매하고 진행
        if stage < n - 1:
            bundle_cost = hint[stage][0]
            bundle_tickets = hint[stage][1:]
            
            bought_inv = list(new_inv)
            for t in bundle_tickets:
                idx = t - 1
                # 힌트권 개수는 최대 n-1개까지만 의미가 있으므로 상한선 설정
                bought_inv[idx] = min(n - 1, bought_inv[idx] + 1)
            
            min_cost = min(min_cost, base_cost + bundle_cost + dfs(stage + 1, tuple(bought_inv)))
            
        return min_cost

    # 초기 인벤토리는 모든 스테이지의 힌트권 개수가 0개인 상태
    initial_inv = tuple([0] * n)
    return dfs(0, initial_inv)