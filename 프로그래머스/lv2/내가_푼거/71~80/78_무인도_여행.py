import sys

sys.setrecursionlimit(20000)

def solution(maps):
    h = len(maps)
    w = len(maps[0])
    dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i, map in enumerate(maps) :
        maps[i] = list(map)

    def travel(start_coord) :
        x, y = start_coord
        cur = int(maps[x][y])
        maps[x][y] = "X"

        for dx, dy in dr :
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= h or ny < 0 or ny >= w :
                continue
            if maps[nx][ny] == "X" :
                continue
            cur += travel((nx, ny))

        return cur
    
    answer = []

    for i in range(h) :
        for j in range(w) :
            cur = maps[i][j]
            if cur == "X" :
                continue
            answer.append(travel((i, j)))

    return sorted(answer) if answer else [-1]
            
print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))
#print(solution(["XXX","XXX","XXX"]))