import sys
sys.setrecursionlimit(100000)

def n_queen(board, row) :
    result = 0
    n = len(board)
    for i in range(n) :
        if i not in board :
            for j in range(row) :
                pre = board[j]
                if abs(i - pre) == abs(row - j):
                    break
            else :
                board[row] = i
                result += n_queen(board, row + 1)
    if board[-1] != -1 :
        result += 1
    board[row - 1] = -1
    return result
    

def solution(n):
    board = [-1] * n

    return n_queen(board, 0)

print(solution(8))