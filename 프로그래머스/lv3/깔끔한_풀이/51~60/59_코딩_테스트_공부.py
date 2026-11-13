def solution(alp, cop, problems):
    # 1. 최종 도달해야 할 목표 알고력과 코딩력 설정
    target_alp = max(max(x[0] for x in problems), alp)
    target_cop = max(max(x[1] for x in problems), cop)
    
    # 2. 2차원 DP 테이블 초기화 (무한대로 설정)
    dp = [[float('inf')] * (target_cop + 1) for _ in range(target_alp + 1)]
    
    # 3. 초기 상태 설정
    dp[alp][cop] = 0

    # 4. DP 순회 (바텀업 방식)
    for i in range(alp, target_alp + 1):
        for j in range(cop, target_cop + 1):
            # (1) 알고력 1 공부하기
            if i < target_alp:
                dp[i + 1][j] = min(dp[i][j] + 1, dp[i + 1][j])
            # (2) 코딩력 1 공부하기
            if j < target_cop:
                dp[i][j + 1] = min(dp[i][j] + 1, dp[i][j + 1])
                
            # (3) 문제 풀기
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if alp_req <= i and cop_req <= j:
                    clear_alp = min(i + alp_rwd, target_alp)
                    clear_cop = min(j + cop_rwd, target_cop)
                    dp[clear_alp][clear_cop] = min(dp[clear_alp][clear_cop], dp[i][j] + cost)

    return dp[target_alp][target_cop]