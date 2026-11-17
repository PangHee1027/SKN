def solution(board, h, w) :
    n, m = len(board), len(board[0])
    dr = ((0, 1), (0, -1), (1, 0), (-1, 0))
    result = 0
    target = board[h][w]
    
    for dx, dy in dr :
        nx, ny = h + dx, w + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m :
            continue
        if board[nx][ny] == target :
            result += 1
    return result
    