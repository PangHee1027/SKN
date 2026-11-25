def solution(m, n, board) :
    rotated_board = [[''] * m for _ in range(n)]
    result = 0
    
    for i in range(m) :
        for j in range(n) :
            rotated_board[j][m - i - 1] = board[i][j]
    
    while True :
        delete = set()
        for i in range(n - 1) :
            for j in range(m - 1) :
                cur = rotated_board[i][j]
                if not cur :
                    break
                if all((rotated_board[i + 1][j + 1] == cur, rotated_board[i + 1][j] == cur, rotated_board[i][j + 1] == cur)) :
                    delete.update({(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)})
        result += len(delete)
        if not delete :
            break
        while delete :
            x, y = delete.pop()
            rotated_board[x][y] = ''
        for i in range(n)  :
            rotated_board[i].sort(key = lambda x : not x)
            
    return result