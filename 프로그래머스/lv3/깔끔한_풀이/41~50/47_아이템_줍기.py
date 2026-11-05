from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
  def draw_rectangle(x1, y1, x2, y2, type):
    for i in range(x1, x2 + 1):
      for j in range(y1, y2 + 1):
        board[i][j] = type

  board = [[0] * 102 for _ in range(102)]
  dr = ((1, 0), (-1, 0), (0, -1), (0, 1))

  # 테두리 채우기 및 내부 파내기
  for x1, y1, x2, y2 in rectangle:
    draw_rectangle(2 * x1, 2 * y1, 2 * x2, 2 * y2, 1)
  for x1, y1, x2, y2 in rectangle:
    draw_rectangle(2 * x1 + 1, 2 * y1 + 1, 2 * x2 - 1, 2 * y2 - 1, 0)

  cx, cy = 2 * characterX, 2 * characterY
  ix, iy = 2 * itemX, 2 * itemY

  dq = deque([(cx, cy)])
  # 거리를 저장하는 2차원 배열을 별도로 관리
  dist = [[0] * 102 for _ in range(102)]
  dist[cx][cy] = 1

  while dq:
    x, y = dq.popleft()

    # 목적지 도달 시 조기 종료
    if x == ix and y == iy:
      return (dist[x][y] - 1) // 2

    for dx, dy in dr:
      nx, ny = x + dx, y + dy
      if board[nx][ny] == 1 and dist[nx][ny] == 0:
        dist[nx][ny] = dist[x][y] + 1
        dq.append((nx, ny))

  return 0