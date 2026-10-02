from collections import deque

def solution(maps):
    h, w = len(maps), len(maps[0])
    # 상, 하, 좌, 우 방향 변위 정의 (루프 밖에서 1회만 정의)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    dq = deque([(0, 0)])
    
    while dq:
        x, y = dq.popleft()
        
        # 목적지에 도달한 경우 즉시 반환 (조기 종료)
        if x == h - 1 and y == w - 1:
            return maps[x][y]
            
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            
            # 맵 범위 내에 있고, 처음 방문하는 길(1)인 경우
            if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                dq.append((nx, ny))
                
    return -1