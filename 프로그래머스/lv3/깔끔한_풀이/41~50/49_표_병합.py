def solution(commands):
  empty = 'EMPTY'
  table = [['EMPTY'] * 51 for _ in range(51)]
  answer = []

  def find_root(r, c):
    path = []
    while isinstance(table[r][c], tuple):
      path.append((r, c))
      r, c = table[r][c]
    # 경로 압축(Path Compression) 적용
    for pr, pc in path:
      table[pr][pc] = (r, c)
    return r, c

  for command in commands:
    command = command.split()
    match command[0]:
      case 'UPDATE':
        if len(command) == 4:
          r, c, v = int(command[1]), int(command[2]), command[3]
          r, c = find_root(r, c)
          table[r][c] = v
        else:
          v1, v2 = command[1], command[2]
          for i in range(1, 51):
            for j in range(1, 51):
              if table[i][j] == v1:
                table[i][j] = v2
      case 'MERGE':
        r1, c1, r2, c2 = (
            int(command[1]),
            int(command[2]),
            int(command[3]),
            int(command[4]),
        )
        r1, c1 = find_root(r1, c1)
        r2, c2 = find_root(r2, c2)
        if r1 == r2 and c1 == c2:
          continue
        value = empty
        if table[r1][c1] != empty:
          value = table[r1][c1]
        elif table[r2][c2] != empty:
          value = table[r2][c2]
        table[r1][c1] = value
        table[r2][c2] = (r1, c1)
      case 'UNMERGE':
        r, c = int(command[1]), int(command[2])
        root_r, root_c = find_root(r, c)
        value = table[root_r][root_c]
        merged_cells = []
        for i in range(1, 51):
          for j in range(1, 51):
            if find_root(i, j) == (root_r, root_c):
              merged_cells.append((i, j))
        for finded_r, finded_c in merged_cells:
          table[finded_r][finded_c] = empty
        table[r][c] = value
      case 'PRINT':
        r, c = int(command[1]), int(command[2])
        r, c = find_root(r, c)
        value = table[r][c]
        answer.append(value)
  return answer