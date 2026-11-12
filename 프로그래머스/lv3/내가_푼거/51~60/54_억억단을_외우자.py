def solution(e, starts):
    dp = [0] * (e + 1)
    for i in range(1, e + 1) :
        for j in range(i, e + 1, i) :
            dp[j] += 1

    answer = []

    dp2 = [0] * (e + 1)
    dp2[-1] = e
    
    max_num, max_count = e, dp[e]
    for i in range(e - 1, 0, -1) :
        count = dp[i]
        if count >= max_count :
            max_num = i
            max_count = count
        dp2[i] = max_num

    for s in starts :
        answer.append(dp2[s])
        
    return answer

print(solution(8, [1,3,7]))