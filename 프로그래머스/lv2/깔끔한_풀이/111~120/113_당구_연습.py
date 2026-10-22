def solution(m, n, startX, startY, balls):
  answer = []

  for x, y in balls:
    cases = []
    # 4가지 기본 벽 대칭 이동 위치 (하, 상, 좌, 우)
    for dx, dy in ((x, -y), (x, 2 * n - y), (-x, y), (2 * m - x, y)):
      distance = (startX - dx) ** 2 + (startY - dy) ** 2
      cases.append(distance)

    # 1. 수직선상 예외 처리 (x 좌표가 같은 경우)
    if startX == x:
      if y < startY:
        cases[0] = float("inf")  # 아래 벽 차단
      else:
        cases[1] = float("inf")  # 위 벽 차단

    # 2. 수평선상 예외 처리 (y 좌표가 같은 경우)
    if startY == y:
      if x < startX:
        cases[2] = float("inf")  # 왼쪽 벽 차단
      else:
        cases[3] = float("inf")  # 오른쪽 벽 차단

    # 3. 대각선 1: (0, 0)과 (m, n)을 잇는 대각선상에 있는 경우
    if startX * (startY - y) == startY * (startX - x):
      distance = float("inf")
      if startX < x:
        distance = (startX + x) ** 2 + (startY + y) ** 2  # (0, 0) 꼭짓점
      else:
        distance = (
            startX - (2 * m - x)
        ) ** 2 + (startY - (2 * n - y)) ** 2  # (m, n) 꼭짓점
      cases.append(distance)

    # 4. 대각선 2: (0, n)과 (m, 0)을 잇는 대각선상에 있는 경우 (추가됨)
    if startX * (y - n) == (startY - n) * x:
      distance = float("inf")
      if startX < x:
        distance = (startX + x) ** 2 + (startY - (2 * n - y)) ** 2  # (0, n) 꼭짓점
      else:
        distance = (
            startX - (2 * m - x)
        ) ** 2 + (startY + y) ** 2  # (m, 0) 꼭짓점
      cases.append(distance)

    answer.append(min(cases))

  return answer