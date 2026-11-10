def solution(N, number) :
    if N == number :
        return 1

    dp = [set() for _ in range(9)]
    n = N
    for i in range(1, 9) :
        dp[i].add(n)
        n = 10 * n + N

    for i in range(2, 9) :
        for j in range(1, i) :
            k = i - j
            for num1 in dp[j] :
                for num2 in dp[k] :
                    if num1 // num2 :
                        dp[i].add(num1 // num2)
                    dp[i].add(num1 + num2)
                    if num1 - num2 > 0 :
                        dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
        if number in dp[i] :
            return i

    return -1

print(solution(5, 12))