from collections import deque
from copy import deepcopy

def solution(maps):
    h, w = len(maps), len(maps[0])
    coordinate = {"S" : (0, 0), "L" : (0, 0), "E" : (0, 0)}

    for i in range(h) :
        maps[i] = list(maps[i])

    start_to_lever = deepcopy(maps)
    lever_to_exit = deepcopy(maps)

    for i in range(h) :
        for j in range(w) :
            if maps[i][j] in ("S", "L", "E") :
                coordinate[maps[i][j]] = (i, j)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    start_x, start_y = coordinate["S"][0], coordinate["S"][1]
    lever_x, lever_y = coordinate["L"][0], coordinate["L"][1]
    exit_x, exit_y = coordinate["E"][0], coordinate["E"][1]

    start_to_lever[start_x][start_y] = 0
    dq = deque([coordinate["S"]])

    while dq :
        x, y = dq.popleft()

        for i, j in moves :
            nx, ny = x + i, y + j
            if 0 <= nx < h and 0 <= ny < w and (start_to_lever[nx][ny] in ("O", "E", "L")):
                start_to_lever[nx][ny] = start_to_lever[x][y] + 1
                dq.append((nx, ny))

    s2l = start_to_lever[lever_x][lever_y]

    if s2l == "L" :
        return -1

    lever_to_exit[lever_x][lever_y] = 0
    dq = deque([coordinate["L"]])

    while dq :
        x, y = dq.popleft()
    
        for i, j in moves :
            nx, ny = x + i, y + j
            if 0 <= nx < h and 0 <= ny < w and (lever_to_exit[nx][ny] in ("O", "E", "S")):
                lever_to_exit[nx][ny] = lever_to_exit[x][y] + 1
                dq.append((nx, ny))

    l2e = lever_to_exit[exit_x][exit_y]
    
    if l2e == "E" :
        return -1
        
    return s2l + l2e

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))