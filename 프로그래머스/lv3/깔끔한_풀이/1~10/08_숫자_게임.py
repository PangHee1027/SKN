def solution(A, B):
  A.sort()
  B.sort()

  score = 0
  a_idx = 0
  b_idx = 0

  # 두 배열을 순회할 포인터가 범위를 벗어나지 않을 때까지 반복
  while a_idx < len(A) and b_idx < len(B):
    # B의 카드가 A의 카드보다 크다면 승점 획득 후 두 카드 모두 다음으로 이동
    if B[b_idx] > A[a_idx]:
      score += 1
      a_idx += 1
      b_idx += 1
    else:
      # B의 카드가 A의 카드보다 작거나 같다면,
      # 이 B 카드는 현재 A[a_idx]를 절대 이길 수 없으므로 버림 (b_idx만 증가)
      # 다음으로 큰 B 카드가 A[a_idx]를 이길 수 있는지 재확인합니다.
      b_idx += 1

  return score