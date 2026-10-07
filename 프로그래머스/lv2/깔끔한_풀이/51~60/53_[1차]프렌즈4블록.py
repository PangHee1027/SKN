def solution(m, n, board):
    answer = 0
    # 전처리: 열(n)을 행으로 변환 및 바닥면을 인덱스 0으로 놓기
    board_preprocessed = [list(col)[::-1] for col in zip(*board)]

    while True:
        drop = set()

        # 1. 2x2 터트릴 블록 탐색
        for i in range(1, n):
            for j in range(1, m):
                block = board_preprocessed[i][j]
                if block != 0 and block == board_preprocessed[i-1][j-1] == board_preprocessed[i][j-1] == board_preprocessed[i-1][j]:
                    drop.update([(i, j), (i, j-1), (i-1, j), (i-1, j-1)])

        # 터트릴 블록이 없으면 종료
        if not drop:
            break

        answer += len(drop)

        # 2. 블록 지우기 (0으로 변경)
        for a, b in drop:
            board_preprocessed[a][b] = 0

        # 3. 블록 떨어뜨리기 (0을 제거한 후 뒤쪽을 0으로 채움)
        for i in range(n):
            new_row = [b for b in board_preprocessed[i] if b != 0]
            board_preprocessed[i] = new_row + [0] * (m - len(new_row))

    return answer