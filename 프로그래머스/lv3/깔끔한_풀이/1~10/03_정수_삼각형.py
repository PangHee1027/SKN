def solution(triangle):
    n = len(triangle)
    # 아래층으로 내려가며 누적합을 갱신합니다.
    for i in range(1, n):
        for j in range(len(triangle[i])):
            # 만약 가장 왼쪽 끝 원소라면, 바로 위(오른쪽 위)에서 내려오는 경우만 존재
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            # 만약 가장 오른쪽 끝 원소라면, 바로 위(왼쪽 위)에서 내려오는 경우만 존재
            elif j == i:
                triangle[i][j] += triangle[i - 1][j - 1]
            # 그 외의 중간 원소들은 왼쪽 위와 오른쪽 위 중 더 큰 값을 선택
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
                
    # 바닥 행에 도달한 누적합들 중 최댓값을 반환합니다.
    return max(triangle[-1])