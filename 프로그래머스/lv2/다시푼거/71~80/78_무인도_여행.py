import sys
sys.setrecursionlimit(100000)

def solution(maps) :
    def dfs(x, y) :
        result = 0
        visited.add((x, y))
        for dx, dy in dr :
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
            if (nx, ny) in visited :
                continue
            if maps[nx][ny] :
                result += dfs(nx, ny)
        result += maps[x][y]
        maps[x][y] = 0
        
        return result
                
    maps = list(map(list, maps))
    n, m = len(maps), len(maps[0])
    dr = ((1, 0), (-1, 0), (0, 1), (0, -1))
    visited = set()
    
    for i, row in enumerate(maps) :
        for j, col in enumerate(row) :
            if col == 'X' :
                maps[i][j] = '0'
    
    for i in range(n) :
        maps[i] = list(map(int, maps[i]))
    
    answer = []
    
    for i in range(n) :
        for j in range(m) :
            if maps[i][j] :
                answer.append(dfs(i, j))
    
    if not answer :
        return [-1]
    
    return sorted(answer)