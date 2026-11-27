from collections import deque

def solution(board) :
    def next_cor(direction, cor) :
        x, y = cor
        dx, dy = direction
        nx, ny = x + dx, y + dy
        if (nx, ny) in block :
            return (x, y)
        return next_cor(direction, (nx, ny))
    
    block = set()
    start, end = (-1, -1), (-1, -1)
    n, m = len(board), len(board[0])
    dr = ((1, 0), (-1, 0), (0, 1), (0, -1))
    board = list(map(list, board))
    
    for i in range(n) :
        block.add((i, -1))
        block.add((i, m))
    for i in range(m) :
        block.add((-1, i))
        block.add((n, i))
    
    for i in range(n) :
        for j in range(m) :
            if board[i][j] == 'R' :
                start = (i, j)
            elif board[i][j] == 'G' :
                end = (i, j)
            elif board[i][j] == 'D' :
                block.add((i, j))
    
    board[start[0]][start[1]] = 0
    dq = deque([start])
        
    while dq :
        cur = dq.popleft()
        cost = board[cur[0]][cur[1]] + 1
        
        for direction in dr :
            nxt = next_cor(direction, cur)
            target = board[nxt[0]][nxt[1]]
            if target in ('.', 'G') or target > cost :
                board[nxt[0]][nxt[1]] = cost
                dq.append(nxt)
                
    if board[end[0]][end[1]] == 'G' :
        return -1
        
    return board[end[0]][end[1]]