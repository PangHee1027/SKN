def solution(board, moves):
    size = len(board)
    stack = []
    answer = 0
    for i in moves :
        current = 0
        for j in range(size) :
            if board[j][i - 1] == 0 :
                continue
            current, board[j][i - 1] = board[j][i - 1], current
            stack.append(current)
            break
    
        if len(stack) >= 2 and stack[-2] == stack[-1] :
            answer += 2
            del stack[-2:]
    
    return answer

# print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))