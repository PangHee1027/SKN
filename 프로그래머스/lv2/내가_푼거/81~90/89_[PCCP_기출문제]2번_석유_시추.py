from collections import deque

def solution(land):
    h = len(land)
    w = len(land[0])
    dr = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    rotated_land = [[0 for _ in range(h)] for _ in range(w)]

    for i in range(h) :
        for j in range(w) :
            rotated_land[j][h - i - 1] = land[i][j]

    h, w = w, h

    for i in range(h) :
        for j in range(w) :
            if not rotated_land[i][j] or rotated_land[i][j] > 1 :
                continue
            count = 1
            dq = deque([(i, j)])
            visited = {(i, j)}
            while dq :
                x, y = dq.popleft()
                rotated_land[x][y] = 0
                for dx, dy in dr :
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= h or ny < 0 or ny >= w :
                        continue
                    if rotated_land[nx][ny] == 1 and (nx, ny) not in visited :
                        dq.append((nx, ny))
                        visited.add((nx, ny))
                        count += 1
            visited_x = set()
            while visited :
                x, y = visited.pop()
                if x not in visited_x :
                    rotated_land[x][y] = count
                    visited_x.add(x)
    for i, row in enumerate(rotated_land) :
        rotated_land[i] = sum(row)
    
    return max(rotated_land)

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))
print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]))