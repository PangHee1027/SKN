def solution(beginning, target) :
    def reverse_row(board, r) :
        for i, c in enumerate(board[r]) :
            board[r][i] = abs(c - 1)
        return board
        
    def check_column(board, c) :
        board_col = [row[c] for row in board]
        target_col = [row[c] for row in target]
        if board_col == target_col :
            return 0
        elif all(a ^ b for a, b in zip(board_col, target_col)) :
            return 1
        else :
            return float('inf')

    def check_board(board) :
        return sum(check_column(board, i) for i in range(m))

    def dfs(board, r, count) :
        reverse_board = reverse_row([[board[i][j] for j in range(m)] for i in range(n)], r)
        if r < n - 1 :
            result1 = dfs(board, r + 1, count)
            result2 = dfs(reverse_board, r + 1, count + 1)
        else :
            result1 = count + check_board(board)
            result2 = count + 1 + check_board(reverse_board)

        return min(result1, result2)

    n = len(beginning)
    m = len(beginning[0])

    result = dfs(beginning, 0, 0)

    return result if result != float('inf') else -1

print(solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]], [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]))
print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 0, 1], [0, 0, 0], [0, 0, 0]]))