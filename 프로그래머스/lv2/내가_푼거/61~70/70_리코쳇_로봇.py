from collections import deque

def solution(board) :
    h = len(board)
    w = len(board[0])

    start = [0, 0]
    target = [0, 0]
    visited = set()

    for i in range(h) :
        board[i] = list(board[i])

    for i in range(h) :
        for j in range(w) :
            if board[i][j] == "R" :
                start = (i, j)
            elif board[i][j] == "G" :
                target = (i, j)

    dq = deque([start])
    board[start[0]][start[1]] = 0
    board[target[0]][target[1]] = -1
    visited.add(start)

    while dq :
        x, y = dq.popleft()
        if (x, y) == target :
            break
        count = board[x][y] + 1
        a = x
        b = y

        while a > 0 :
            if board[a - 1][b] == "D" :
                break
            a -= 1
        up = (a, b)
        a = x
        while a < h - 1 :
            if board[a + 1][b] == "D" :
                break
            a += 1
        down = (a, b)
        a = x
        while b > 0 :
            if board[a][b - 1] == "D" :
                break
            b -= 1
        left = (a, b)
        b = y
        while b < w - 1 :
            if board[a][b + 1] == "D" :
                break
            b += 1
        right = (a, b)
        for coor in [up, down, left, right] :
            if coor not in visited or board[coor[0]][coor[1]] > count :
                visited.add(coor)
                board[coor[0]][coor[1]] = count
                dq.append(coor)
        
    return board[target[0]][target[1]]

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
# print(solution([".D.R", "....", ".G..", "...D"]))