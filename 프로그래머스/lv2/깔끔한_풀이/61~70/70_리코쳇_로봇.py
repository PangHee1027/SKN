from collections import deque

def solution(board):
    h = len(board)
    w = len(board[0])

    start = (0, 0)
    target = (0, 0)
    
    # 1번 방법 적용: 원본 board를 훼손하지 않고, 거리 및 방문 여부를 관리할 dist 배열 생성 (-1로 초기화)
    dist = [[-1] * w for _ in range(h)]

    # 시작점(R)과 도착점(G) 위치 찾기
    for i in range(h):
        for j in range(w):
            if board[i][j] == "R":
                start = (i, j)
            elif board[i][j] == "G":
                target = (i, j)

    dq = deque([start])
    dist[start[0]][start[1]] = 0  # 시작점 거리는 0으로 설정

    # 1번 방법 적용: 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while dq:
        x, y = dq.popleft()

        # 목표 지점에 도달했다면 현재까지의 최단 거리 반환
        if (x, y) == target:
            return dist[x][y]

        current_dist = dist[x][y]

        # 4방향으로 미끄러지기 탐색
        for dx, dy in directions:
            nx, ny = x, y

            # 벽이나 장애물("D")에 부딪힐 때까지 한 방향으로 계속 전진
            while 0 <= nx + dx < h and 0 <= ny + dy < w and board[nx + dx][ny + dy] != "D":
                nx += dx
                ny += dy

            # 미끄러져 멈춘 위치가 아직 방문하지 않았거나, 더 짧은 경로로 도달할 수 있는 경우
            if dist[nx][ny] == -1 or dist[nx][ny] > current_dist + 1:
                dist[nx][ny] = current_dist + 1
                dq.append((nx, ny))

    # 큐가 빌 때까지 목표 지점에 도달하지 못한 경우
    return -1