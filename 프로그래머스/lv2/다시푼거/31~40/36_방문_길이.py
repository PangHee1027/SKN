def solution(dirs):
    dr = {'U' : (-1, 0), 'D' : (1, 0), 'R' : (0, 1), 'L' : (0, -1)}
    visited = set()
    x, y = 0, 0
    for d in dirs :
        dx, dy = dr[d]
        nx, ny = x + dx, y + dy
        if nx < -5 or nx > 5 or ny < -5 or ny > 5 :
            continue
        visited.add((x, y, nx, ny))
        visited.add((nx, ny, x, y))
        x, y = nx, ny
        
    return len(visited) // 2