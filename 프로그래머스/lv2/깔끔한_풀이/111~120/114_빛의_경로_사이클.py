def solution(grid):
  state_dict = {
      "S": {"up": "up", "down": "down", "left": "left", "right": "right"},
      "L": {"up": "left", "down": "right", "left": "down", "right": "up"},
      "R": {"up": "right", "down": "left", "left": "up", "right": "down"},
  }

  n = len(grid)
  m = len(grid[0])

  state_count = {}
  answer = []

  for i in range(n):
    for j in range(m):
      for direction in ("up", "down", "left", "right"):
        state = ((i, j), direction)

        # state_count에 이미 존재한다면, 이전 탐색에서 이미 지나친 사이클의 일부임
        if state in state_count:
          continue

        x, y, d, count = i, j, direction, 0
        while True:
          count += 1
          s = ((x, y), d)

          if s in state_count:
            cycle = count - state_count[s]
            answer.append(cycle)
            break

          state_count[s] = count
          d = state_dict[grid[x][y]][d]

          match d:
            case "up":
              x = (x - 1) % n
            case "down":
              x = (x + 1) % n
            case "left":
              y = (y - 1) % m
            case "right":
              y = (y + 1) % m

  return sorted(answer)