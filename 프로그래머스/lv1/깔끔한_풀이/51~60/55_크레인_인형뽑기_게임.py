def solution(board, moves):
    # 각 열별 인형 스택 생성 (아래쪽 인형부터 쌓이도록 역순 탐색)
    cols = [[] for _ in range(len(board))]
    for row in range(len(board) - 1, -1, -1):
        for col in range(len(board)):
            if board[row][col] != 0:
                cols[col].append(board[row][col])

    basket = []
    answer = 0

    for move in moves:
        col_idx = move - 1
        if cols[col_idx]:  # 해당 열에 인형이 존재하는 경우
            doll = cols[col_idx].pop()
            if basket and basket[-1] == doll:
                basket.pop()
                answer += 2
            else:
                basket.append(doll)

    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])