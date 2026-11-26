from collections import deque

def solution(maps) :
    def bfs(start, end) :
        visited = {start}
        dq = deque([(start, 0)])
        
        while dq :
            (x, y), cost = dq.popleft()
            for dx, dy in dr :
                nx, ny = dx + x, dy + y
                if nx < 0 or nx >= n or ny < 0 or ny >= m :
                    continue
                if (nx, ny) == end :
                    return cost + 1
                if (nx, ny) not in visited and maps[nx][ny] != 'X':
                    dq.append(((nx, ny), cost + 1))
                    visited.add((nx, ny))
            
        return 0
        
    n, m = len(maps), len(maps[0])
    start, end, lever = (-1, -1), (-1, -1), (-1, -1)
    dr = ((0, 1), (0, -1), (1, 0), (-1, 0))
    for i in range(n) :
        for j in range(m) :
            cur = maps[i][j]
            if cur == 'S' :
                start = (i, j)
            elif cur == 'E' :
                end = (i, j)
            elif cur == 'L' :
                lever = (i, j)
    
    s2l = bfs(start, lever)
    l2e = bfs(lever, end)
    
    if not s2l or not l2e :
        return -1
    
    return s2l + l2e