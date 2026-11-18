def solution(board, moves):
    n = len(board)
    rotate_board = [[0] * n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            rotate_board[j][n - i - 1] = board[i][j]
    for i in range(n) :
        while rotate_board[i] and not rotate_board[i][-1] :
            rotate_board[i].pop()
    answer = 0
    stack = []
    for i in moves :
        if rotate_board[i - 1] :
            stack.append(rotate_board[i - 1].pop())
        while len(stack) >= 2 and stack[-1] == stack[-2] :
            stack.pop()
            stack.pop()
            answer += 2
    return answer