from collections import deque

def solution(board) :
    def get_ax_ay(x, y, state) :
        ax, ay = x, y
        if state :
            ax += 1
        else :
            ay += 1
        return ax, ay
    
    def check_position(x, y) :
        if x >= n or x < 0 or y >= n or y < 0 :
            return True
        if board[x][y] :
            return True
        return False
    
    # (x, y), state(0 = 가로, 1 = 세로)
    # state = 0일 때 두번째 칸 -> (x, y + 1)
    # state = 1일 때 두번째 칸 -> (x + 1, y)
    dr = ((1, 0), (0, 1), (0, -1), (-1, 0))
    n = len(board)
    dq = deque([((0, 0), 0, 0)])
    visited = set()
    visited.add(((0, 0), 0))
    rotate = {
                0 : [{'state' : 1, 'cor' : (0, 1), 'check' : (1, 0)}, {'state' : 1, 'cor' : (-1, 1), 'check' : (-1, 0)}, 
                   {'state' : 1, 'cor' : (0, 0), 'check' : (1, 1)}, {'state' : 1, 'cor' : (-1, 0), 'check' : (-1, 1)}],
                1 : [{'state' : 0, 'cor' : (0, -1), 'check' : (1, -1)}, {'state' : 0, 'cor' : (1, -1), 'check' : (0, -1)}, 
                   {'state' : 0, 'cor' : (0, 0), 'check' : (1, 1)}, {'state' : 0, 'cor' : (1, 0), 'check' : (0, 1)}]
            }

    while dq :
        cur, state, time = dq.popleft()
        x, y = cur
        ax, ay = get_ax_ay(x, y, state)
        if ax == n - 1 and ay == n - 1 :
            return time
        for dx, dy in dr :
            nx, ny = x + dx, y + dy
            nax, nay = get_ax_ay(nx, ny, state)
            if check_position(nx, ny) or check_position(nax, nay) :
                continue
            if ((nx, ny), state) in visited :
                continue
            dq.append(((nx, ny), state, time + 1))
            visited.add(((nx, ny), state))
        for nxt_rotate in rotate[state] :
            n_state, n_dr, check = nxt_rotate.values()
            dx, dy = n_dr
            nx, ny = x + dx, y + dy
            nax, nay = get_ax_ay(nx, ny, n_state)
            cx, cy = x + check[0], y + check[1]
            if check_position(nx, ny) or check_position(nax, nay) or check_position(cx, cy):
                continue
            if ((nx, ny), n_state) in visited :
                continue
            dq.append(((nx, ny), n_state, time + 1))
            visited.add(((nx, ny), n_state))

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))