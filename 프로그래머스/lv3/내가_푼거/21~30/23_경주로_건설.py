from collections import deque

def solution(board) :
    n = len(board)
    cost_list = [[[float('inf') ] * 4 for _ in range(n)] for _ in range(n)]
    cost_list[0][0] = [0] * 4
    dr_dict = {'d' : (1, 0), 'u' : (-1, 0), 'r' : (0, 1), 'l' : (0, -1)}
    can_go = {'d' : ['d', 'r', 'l'], 'u' : ['u', 'r', 'l'], 'l' : ['d', 'l', 'u'], 'r' : ['d', 'r', 'u']}
    d_idx = {'d' : 0, 'u' : 1, 'l' : 2, 'r' : 3, 0 : 'd', 1 : 'u', 2 : 'l', 3 : 'r'}
    dq = deque([(0, 0, 'd'), (0, 0, 'r')])

    while dq :
        x, y, direction = dq.popleft()
        for d in can_go[direction] :
            dx, dy = dr_dict[d]
            nx, ny = x + dx, y + dy
            if nx >= n or nx < 0 or ny >= n or ny < 0 :
                continue
            next_cost = cost_list[x][y][d_idx[direction]] + (100 if d == direction else 600)
            if cost_list[nx][ny][d_idx[d]] > next_cost and board[nx][ny] != 1:
                cost_list[nx][ny][d_idx[d]] = next_cost
                dq.append((nx, ny, d))
    
    return min(cost_list[n - 1][n - 1])

#print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]])) # 900
print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]])) # 3800
#print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]])) # 2100
#print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]])) # 3200
