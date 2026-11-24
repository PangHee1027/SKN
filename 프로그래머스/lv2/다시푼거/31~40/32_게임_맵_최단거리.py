from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dr = ((0, 1), (0, -1), (1, 0), (-1, 0))
    visited = {(0, 0)}
    dq = deque([(0, 0, 1)])
    while dq :
        x, y, cost = dq.popleft()
        for dx, dy in dr :
            nx, ny = x + dx, y + dy
            if (nx, ny) == (n - 1, m - 1) :
                return cost + 1
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
            if not maps[nx][ny] or (nx, ny) in visited :
                continue
            dq.append((nx, ny, cost + 1))
            visited.add((nx, ny))
    return -1