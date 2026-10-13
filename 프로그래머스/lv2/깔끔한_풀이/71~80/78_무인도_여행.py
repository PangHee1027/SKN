from collections import deque

def solution(maps):
    h = len(maps)
    w = len(maps[0])
    dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 문자열 배열을 리스트로 변환하여 수정 가능하게 만듦
    board = [list(row) for row in maps]
    answer = []
    
    for i in range(h):
        for j in range(w):
            # 방문하지 않은 땅('X'가 아님)을 발견하면 BFS 시작
            if board[i][j] != "X":
                current_food = int(board[i][j])
                board[i][j] = "X"  # 방문 처리
                
                queue = deque([(i, j)])
                while queue:
                    x, y = queue.popleft()
                    
                    for dx, dy in dr:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != "X":
                            current_food += int(board[nx][ny])
                            board[nx][ny] = "X"  # 방문 처리
                            queue.append((nx, ny))
                            
                answer.append(current_food)
                
    return sorted(answer) if answer else [-1]