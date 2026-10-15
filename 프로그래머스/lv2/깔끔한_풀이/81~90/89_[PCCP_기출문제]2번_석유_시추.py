from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    visited = [[False] * m for _ in range(n)]
    dr = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # 각 열별로 얻을 수 있는 총 석유량을 저장할 리스트
    column_oil = [0] * m

    for i in range(n):
        for j in range(m):
            # 석유가 있고 아직 방문하지 않은 칸인 경우 BFS 시작
            if land[i][j] == 1 and not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = True
                
                size = 0
                cols = set() # 이 석유 덩어리가 지나가는 열들을 저장
                
                while q:
                    r, c = q.popleft()
                    size += 1
                    cols.add(c)
                    
                    for dx, dy in dr:
                        nr, nc = r + dx, c + dy
                        if 0 <= nr < n and 0 <= nc < m:
                            if land[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                q.append((nr, nc))
                
                # 이 석유 덩어리가 닿는 모든 열에 덩어리 크기(size)를 합산
                for c in cols:
                    column_oil[c] += size

    return max(column_oil)