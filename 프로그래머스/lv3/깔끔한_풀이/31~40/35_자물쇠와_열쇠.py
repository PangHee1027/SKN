def solution(key, lock):
  key_size = len(key)
  lock_size = len(lock)

  # 1. 파이썬의 zip과 슬라이싱을 활용한 간결하고 직관적인 90도 회전 함수
  def rotate_key(k):
    return [list(row) for row in zip(*k[::-1])]

  # 2. 검증 로직을 별도의 함수로 분리하여 모듈화
  def check(offset_r, offset_c, rotated_key):
    # 자물쇠 크기의 매트릭스를 생성하고 열쇠가 겹치는 영역을 반영
    matrix = [[0] * lock_size for _ in range(lock_size)]
    for i in range(key_size):
      for j in range(key_size):
        r = i + offset_r
        c = j + offset_c
        if 0 <= r < lock_size and 0 <= c < lock_size:
          matrix[r][c] = rotated_key[i][j]

    # 자물쇠의 모든 홈이 채워졌고 돌기끼리 충돌하지 않는지 검사
    for i in range(lock_size):
      for j in range(lock_size):
        # 자물쇠 칸과 매트릭스 칸의 상태가 같으면 안 됨 (둘 다 0이거나 둘 다 1이면 오류)
        if lock[i][j] == matrix[i][j]:
          return False
    return True

  current_key = key
  # 총 4번 회전 (0도, 90도, 180도, 270도)
  for _ in range(4):
    # 열쇠를 자물쇠 상하좌우 모든 방향으로 이동시켜 봄
    for r in range(-key_size + 1, lock_size):
      for c in range(-key_size + 1, lock_size):
        if check(r, c, current_key):
          return True
    current_key = rotate_key(current_key)

  return False