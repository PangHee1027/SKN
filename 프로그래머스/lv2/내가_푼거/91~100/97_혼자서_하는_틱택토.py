def solution(board):
    o_count, x_count = 0, 0
    for i in range(3) :
        for j in range(3) :
            if board[i][j] == "O" :
                o_count += 1
            elif board[i][j] == "X" :
                x_count += 1

    if o_count - x_count not in [0, 1] :
        return 0

    ls = []

    ls += [list(board[i]) for i in range(3)]
    ls += [[board[j][i] for j in range(3)] for i in range(3)]
    ls += [[board[i][i] for i in range(3)], [board[2 - i][i] for i in range(3)]]

    if any(x == ["O", "O", "O"] for x in ls) :
        if o_count != x_count + 1 :
            return 0
    if any(x == ["X", "X", "X"] for x in ls) :
        if o_count != x_count :
            return 0
        
    return 1

print(solution(["O.X", ".O.", "..X"]))
print(solution(["OOO", "...", "XXX"]))
print(solution(["...", ".X.", "..."]))
print(solution(["...", "...", "..."]))