repeat = int(input())

def best_score(n, stickers) :
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0], dp[0][1] = stickers[0][0], stickers[0][1]

    for i in range(1, n) :
        if i == 1 :
            dp[i][0] = stickers[i][0] + dp[i - 1][1]
            dp[i][1] = stickers[i][1] + dp[i - 1][0]
            continue
        dp[i][0] = max(dp[i - 2][1], dp[i - 1][1]) + stickers[i][0]
        dp[i][1] = max(dp[i - 2][0], dp[i - 1][0]) + stickers[i][1]
        
    return max(dp[-1])

for _ in range(repeat) :
    n = int(input())
    stickers = [[] for _ in range(n)]
    for _ in range(2) :
        for i, sticker in enumerate(map(int, input().split())) :
            stickers[i].append(sticker)
    print(best_score(n, stickers))