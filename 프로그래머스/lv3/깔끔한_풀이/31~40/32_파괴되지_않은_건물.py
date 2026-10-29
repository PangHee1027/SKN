def solution(board, skill):
    m, n = len(board), len(board[0])
    # 모서리 및 바깥쪽(r2+1, c2+1) 접근을 위해 (m + 1) x (n + 1) 크기로 생성
    diff = [[0] * (n + 1) for _ in range(m + 1)]

    # 1. 차이 배열(Difference Array)에 공격/회복 기록 O(1)
    for type, r1, c1, r2, c2, degree in skill:
        val = degree if type == 2 else -degree
        diff[r1][c1] += val
        diff[r1][c2 + 1] -= val
        diff[r2 + 1][c1] -= val
        diff[r2 + 1][c2 + 1] += val

    # 2. 가로 방향 누적합 계산
    for i in range(m + 1):
        for j in range(1, n + 1):
            diff[i][j] += diff[i][j - 1]

    # 3. 세로 방향 누적합 계산
    for j in range(n + 1):
        for i in range(1, m + 1):
            diff[i][j] += diff[i - 1][j]

    # 4. 기존 board와 합산하여 파괴되지 않은 건물 카운트
    not_broken = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] + diff[i][j] > 0:
                not_broken += 1

    return not_broken