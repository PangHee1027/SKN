def solution(target):
    dp = [[] for _ in range(target + 1)] 
    
    # 1다트로 얻을 수 있는 점수와 [다트 수, 싱글/불 횟수] 매핑
    score_dict = {}
    for x in range(1, 21):
        score_dict[x] = [1, 1]      # 싱글
        score_dict[x * 2] = [1, 0]  # 더블
        score_dict[x * 3] = [1, 0]  # 트리플
    score_dict[50] = [1, 1]         # 불
    
    score_set = set(score_dict.keys())
    
    for i in range(1, target + 1):
        if i in score_set:
            dp[i] = score_dict[i]
            continue
            
        best_state = [float('inf'), float('inf')]
        for score in score_set:
            remain = i - score
            if remain <= 0 or not dp[remain]:
                continue
                
            cur_state = [dp[remain][0] + score_dict[score][0], dp[remain][1] + score_dict[score][1]]
            
            if best_state[0] > cur_state[0]:
                best_state = cur_state
            elif best_state[0] == cur_state[0] and best_state[1] < cur_state[1]:
                best_state = cur_state
                
        dp[i] = best_state

    return dp[-1]