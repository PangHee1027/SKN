from collections import deque

def solution(maps):
    h = len(maps)
    w = len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dq = deque()
    dq.append((0,0))

    while dq:
        x, y = dq.popleft()
        for d_x, d_y in list(zip(dx, dy)) :
            if not (0 <= x + d_x < h and 0 <= y + d_y < w) :
                continue
            if maps[x + d_x][y + d_y] == 1 :
                dq.append((x + d_x, y + d_y))
                maps[x + d_x][y + d_y] = maps[x][y] + 1

    return -1 if maps[h - 1][w - 1] == 1 else maps[h - 1][w - 1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))