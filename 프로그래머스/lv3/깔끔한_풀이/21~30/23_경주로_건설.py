import heapq

def solution(board):
    n = len(board)
    # 3차원 비용 배열 초기화 (상, 하, 좌, 우)
    cost_list = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    
    # 방향 및 좌표 설정
    dr_dict = {'u': (-1, 0), 'd': (1, 0), 'l': (0, -1), 'r': (0, 1)}
    can_go = {
        'u': ['u', 'l', 'r'],
        'd': ['d', 'l', 'r'],
        'l': ['l', 'u', 'd'],
        'r': ['r', 'u', 'd']
    }
    d_idx = {'u': 0, 'd': 1, 'l': 2, 'r': 3}
    
    # 우선순위 큐 (heapq) 사용: (누적 비용, x, y, 방향)
    hq = []
    # 시작점에서 아래쪽과 오른쪽으로 출발하는 경우를 미리 큐에 넣고 시작
    heapq.heappush(hq, (0, 0, 0, 'd'))
    heapq.heappush(hq, (0, 0, 0, 'r'))
    cost_list[0][0][d_idx['d']] = 0
    cost_list[0][0][d_idx['r']] = 0

    while hq:
        cost, x, y, direction = heapq.heappop(hq)

        # 이미 더 작은 비용으로 방문한 적이 있다면 스킵 (가지치기)
        if cost_list[x][y][d_idx[direction]] < cost:
            continue

        for d in can_go[direction]:
            dx, dy = dr_dict[d]
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == 1:
                continue

            # 직선 도로는 100원, 코너는 600원(직선 100원 + 추가 500원)
            next_cost = cost + (100 if d == direction else 600)

            if cost_list[nx][ny][d_idx[d]] > next_cost:
                cost_list[nx][ny][d_idx[d]] = next_cost
                heapq.heappush(hq, (next_cost, nx, ny, d))

    return min(cost_list[n - 1][n - 1])