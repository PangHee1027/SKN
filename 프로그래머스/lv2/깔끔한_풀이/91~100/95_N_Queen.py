import sys
sys.setrecursionlimit(100000)

def solution(n):
    answer = 0
    board = [-1] * n

    def dfs(row):
        nonlocal answer
        # 1. 기저 조건: 모든 행에 퀸을 다 놓았을 때
        if row == n:
            answer += 1
            return

        for col in range(n):
            # 2. 유효성 검사 (같은 열, 대각선 체크)
            is_valid = True
            for j in range(row):
                if board[j] == col or abs(board[j] - col) == abs(j - row):
                    is_valid = False
                    break
            
            # 3. 유효하다면 퀸을 놓고 다음 행으로 진행
            if is_valid:
                board[row] = col
                dfs(row + 1)
                board[row] = -1  # 4. 백트래킹 (원상복구)

    dfs(0)
    return answer