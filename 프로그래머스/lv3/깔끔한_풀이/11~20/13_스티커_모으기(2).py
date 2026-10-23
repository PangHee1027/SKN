def solution(sticker):
    n = len(sticker)
    
    if n <= 3 :
        return max(sticker)

    # 1. 첫 번째 스티커를 뗄 경우 (마지막 스티커 사용 불가 -> 길이를 n - 1로 제한)
    dp1 = [0] * (n - 1)
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]  # 첫 번째를 골랐으므로 두 번째는 선택 불가 (값을 그대로 유지)
    
    for i in range(2, n - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])
    
    # 2. 첫 번째 스티커를 떼지 않을 경우 (마지막 스티커 사용 가능 -> 전체 n개 사용)
    dp2 = [0] * n
    dp2[0] = 0
    dp2[1] = sticker[1]  # 첫 번째를 안 골랐으므로 두 번째부터 시작 가능
    
    for i in range(2, n):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    # 각각의 마지막 원소(`-1`)를 비교
    return max(dp1[-1], dp2[-1])