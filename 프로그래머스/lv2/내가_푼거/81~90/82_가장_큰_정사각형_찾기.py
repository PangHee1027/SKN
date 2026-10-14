def solution(board):
    h = len(board)
    w = len(board[0])
    max_len = 0
    dr = [(0, -1), (-1, 0), (-1, -1)]

    for i in range (h) :
        for j in range(w) :
            if not board[i][j] :
                continue
            if i == 0 or j == 0 :
                continue
            len_list = []
            x, y = i, j
            for dx, dy in dr :
                length = 1
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 :
                    len_list.append(1)
                    continue
                if not board[nx][ny] :
                    len_list.append(1)
                    continue
                len_list.append(board[nx][ny] + 1)
            if len_list :
                board[i][j] = min(len_list)

    all = []

    for row in board :
        all += row

    return max(all) ** 2
    # return all

print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))