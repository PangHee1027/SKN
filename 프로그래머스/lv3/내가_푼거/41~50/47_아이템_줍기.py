from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY) :
    def draw_rectangle(x1, y1, x2, y2, type) :
        for i in range(x1, x2 + 1) :
            for j in range(y1, y2 + 1) :
                board[i][j] = type
    
    board = [[0] * 102 for _ in range(102)]
    dr = ((1, 0), (-1, 0), (0, -1), (0, 1))

    for x1, y1, x2, y2 in rectangle :
        draw_rectangle(2 * x1, 2 * y1, 2 * x2, 2 * y2, 1)
    for x1, y1, x2, y2 in rectangle :
        draw_rectangle(2 * x1 + 1, 2 * y1 + 1, 2 * x2 - 1, 2 * y2 - 1, 0)

    dq = deque([(2 * characterX, 2 * characterY)])
    visited = {(2 * characterX, 2 * characterY)}

    while dq :
        x, y = dq.popleft()
        for dx, dy in dr :
            nx, ny = x + dx, y + dy
            if board[nx][ny] and (nx, ny) not in visited :
                dq.append((nx, ny))
                visited.add((nx, ny))
                board[nx][ny] += board[x][y]

    return board[itemX * 2][itemY * 2] // 2
                    

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)) # 17
print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1)) # 11
print(solution([[1, 1, 5, 7]], 1, 1, 4, 7)) # 9
print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10)) # 15
print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3)) # 10