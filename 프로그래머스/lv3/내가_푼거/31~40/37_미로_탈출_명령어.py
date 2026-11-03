import sys
from itertools import product
sys.setrecursionlimit(100000)

def solution(n, m, x, y, r, c, k):
    x, y, r, c = x - 1, y - 1, r - 1, c - 1
    board = [['.'] * m for _ in range(n)]
    dr = {'d' : (1, 0), 'l' : (0, -1), 'r' : (0, 1), 'u' :(-1, 0)}
    board[x][y], board[r][c] = 's', 'e'

    def dfs(cur_route, cur_x, cur_y) :
        if len(cur_route) == k :
            if board[cur_x][cur_y] == 'e' :
                return cur_route
            else :
                return 
        min_distance = abs(cur_x - r) + abs(cur_y - c)
        remain = k - len(cur_route)
        if min_distance > remain or (remain - min_distance) % 2 :
            return
        for cmd, d in dr.items() :
            dx, dy = d
            nx, ny = cur_x + dx, cur_y + dy
            if nx >= n or nx < 0 or ny >= m or ny < 0 :
                continue
            next_route = cur_route + cmd
            result = dfs(next_route, nx, ny)
            if result :
                return result

    result = dfs('', x, y)
    if result :
        return result

    return 'impossible'

print(solution(3, 4, 2, 3, 3, 1, 5))