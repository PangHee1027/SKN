def solution(rows, columns, queries):
    # 1부터 rows * columns까지의 숫자가 담긴 2차원 행렬 생성
    board = [[j + i * columns for j in range(1, columns + 1)] for i in range(rows)]
    answer = []

    for x1, y1, x2, y2 in queries:
        # 1-based index를 0-based index로 변환
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        
        # 1. 테두리의 요소들을 시계 방향 순서대로 추출
        top = board[x1][y1:y2 + 1]
        right = [board[r][y2] for r in range(x1 + 1, x2 + 1)]
        bottom = board[x2][y1:y2][::-1]  # 오른쪽에서 왼쪽 방향이므로 뒤집음
        left = [board[r][y1] for r in range(x2 - 1, x1, -1)]  # 아래에서 위 방향이므로 뒤집음
        
        # 하나의 테두리 리스트로 결합
        border = top + right + bottom + left
        
        # 2. 이번 회전에서 바뀐 숫자들 중 최솟값을 정답에 추가
        answer.append(min(border))
        
        # 3. 시계 방향으로 한 칸 회전 (마지막 원소가 맨 앞으로 이동)
        rotated = [border[-1]] + border[:-1]
        
        # 4. 회전된 값들을 다시 보드의 테두리 위치에 차례대로 반영
        idx = 0
        for i in range(y1, y2 + 1):
            board[x1][i] = rotated[idx]
            idx += 1
        for r in range(x1 + 1, x2 + 1):
            board[r][y2] = rotated[idx]
            idx += 1
        for i in range(y2 - 1, y1 - 1, -1):
            board[x2][i] = rotated[idx]
            idx += 1
        for r in range(x2 - 1, x1, -1):
            board[r][y1] = rotated[idx]
            idx += 1

    return answer