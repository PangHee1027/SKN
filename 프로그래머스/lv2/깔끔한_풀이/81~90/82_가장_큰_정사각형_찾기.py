def solution(board):
    h = len(board)
    w = len(board[0])
    max_len = 0
    
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                # 첫 행이나 첫 열이 아닐 때만 DP 점화식 적용
                if i > 0 and j > 0:
                    board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                
                # 최대 변의 길이 갱신
                max_len = max(max_len, board[i][j])

    return max_len ** 2