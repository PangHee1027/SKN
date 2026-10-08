from collections import deque


def solution(maps):
  h, w = len(maps), len(maps[0])

  # 1. 시작점(S), 레버(L), 출구(E) 좌표 탐색
  for i in range(h):
    for j in range(w):
      if maps[i][j] == "S":
        start = (i, j)
      elif maps[i][j] == "L":
        lever = (i, j)
      elif maps[i][j] == "E":
        exit_pos = (i, j)

  # 2. 범용 BFS 탐색 함수 (출발지 -> 목적지 최단 거리 계산)
  def bfs(start_pos, target_pos):
    queue = deque([(start_pos[0], start_pos[1], 0)])
    visited = [[False] * w for _ in range(h)]
    visited[start_pos[0]][start_pos[1]] = True

    while queue:
      x, y, dist = queue.popleft()

      # 목적지에 도달한 경우 즉시 거리 반환 (조기 종료)
      if (x, y) == target_pos:
        return dist

      for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy

        # 범위 내에 있고, 벽('X')이 아니며, 방문하지 않은 위치 탐색
        if (
            0 <= nx < h
            and 0 <= ny < w
            and not visited[nx][ny]
            and maps[nx][ny] != "X"
        ):
          visited[nx][ny] = True
          queue.append((nx, ny, dist + 1))

    return -1  # 목적지에 도달할 수 없는 경우

  # 3. S -> L 최단 거리 계산
  path1 = bfs(start, lever)
  if path1 == -1:
    return -1

  # 4. L -> E 최단 거리 계산
  path2 = bfs(lever, exit_pos)
  if path2 == -1:
    return -1

  return path1 + path2