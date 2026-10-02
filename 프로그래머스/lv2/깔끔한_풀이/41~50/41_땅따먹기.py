def solution(land):
    h = len(land)
    w = len(land[0])  # 열의 개수 (가변적)

    for i in range(1, h):
        prev_row = land[i - 1]
        
        # 1. 이전 행의 1등 값, 1등의 열 인덱스, 2등 값을 O(M)으로 구함
        max1_idx = prev_row.index(max(prev_row))
        max1_val = prev_row[max1_idx]
        
        # 1등 열을 제외한 나머지 중 최댓값 (2등 값)
        max2_val = max(prev_row[:max1_idx] + prev_row[max1_idx + 1:])

        # 2. 현재 행의 각 열 갱신 (O(M))
        for j in range(w):
            if j == max1_idx:
                land[i][j] += max2_val  # 1등 열과 겹치면 2등 값 사용
            else:
                land[i][j] += max1_val  # 안 겹치면 1등 값 사용

    return max(land[-1])