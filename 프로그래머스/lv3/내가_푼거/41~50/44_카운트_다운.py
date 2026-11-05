def solution(target) :
    dp = [[] for _ in range(target + 1)] 
    score_dict = {x : [1, 0] for x in range(3, 61, 3)} | {x : [1, 0] for x in range(2, 41, 2)} | {x : [1, 1] for x in range(1, 21)} | {50 : [1, 1]}
    score_item = sorted([item for item in score_dict.items()], key = lambda x : (-x[0], -x[1][1]))
    score_key = [x for x, _ in score_item]
    
    for i in range(1, target + 1) :
        if i in score_key :
            dp[i] = score_dict[i]
            continue
        best_state = [float('inf'), float('inf')]
        for score in score_key :
            remain = i - score
            if remain <= 0 :
                continue
            cur_state = [x + y for x, y in zip(dp[remain], score_dict[score])]
            if best_state[0] > cur_state[0] :
                best_state = cur_state
            elif best_state[0] == cur_state[0] and best_state[1] < cur_state[1] :
                best_state = cur_state
        dp[i] = best_state

    return dp[-1]

#print(solution(21))
print(solution(58))