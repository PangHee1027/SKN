def solution(m, n, puddles) :
    board = [[0 for _ in range(m)] for _ in range(n)]
    for puddle in puddles :
        y, x = puddle
        board[x - 1][y - 1] = "X"

    board[0][0] = 1

    for i in range(n) :
        for j in range(m) :
            cur = board[i][j]
            if cur == "X" :
                continue
            if i < n - 1 :
                if board[i + 1][j] != "X":
                    board[i + 1][j] += cur
            if j < m - 1 :      
                if board[i][j + 1] != "X" :
                    board[i][j + 1] += cur

    return board[n - 1][m - 1] % 1000000007

print(solution(4, 3, [[2, 2]]))