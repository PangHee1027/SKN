def solution(n, m, x, y, r, c, k):
  # 0-based index로 변환
  x, y, r, c = x - 1, y - 1, r - 1, c - 1

  # 1. 초기 도달 가능성 검사 (거리 및 홀짝성)
  dist = abs(x - r) + abs(y - c)
  if k < dist or (k - dist) % 2 != 0:
    return 'impossible'

  answer = []
  # 사전순 우선순위: 'd'(아래), 'l'(왼쪽), 'r'(오른쪽), 'u'(위)
  directions = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]

  cur_x, cur_y = x, y
  rem = k

  # 2. k번 이동하는 동안 매 스텝마다 가장 빠른 사전순 방향 선택
  for _ in range(k):
    moved = False
    for cmd, dx, dy in directions:
      nx, ny = cur_x + dx, cur_y + dy

      # 격자 범위를 벗어나지 않는지 확인
      if 0 <= nx < n and 0 <= ny < m:
        # 이동 후 목적지까지의 남은 최단 거리
        next_dist = abs(nx - r) + abs(ny - c)

        # 남은 스텝(rem - 1) 내에 도달 가능하고 홀짝성(패리티) 조건이 맞는 경우
        if next_dist <= rem - 1 and (rem - 1 - next_dist) % 2 == 0:
          answer.append(cmd)
          cur_x, cur_y = nx, ny
          rem -= 1
          moved = True
          break

    if not moved:
      return 'impossible'

  return ''.join(answer)