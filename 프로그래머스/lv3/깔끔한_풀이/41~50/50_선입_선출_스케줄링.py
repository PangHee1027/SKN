def solution(n, cores):
  # 작업 개수가 코어 개수보다 적거나 같으면 바로 코어 번호 반환
  if n <= len(cores):
    return n

  left, right = 0, max(cores) * n
  while left < right:
    mid = (left + right) // 2
    processing = len(cores) + sum(mid // x for x in cores)
    if processing >= n:
      right = mid
    else:
      left = mid + 1

  processed = len(cores) + sum((left - 1) // x for x in cores)

  for i, core in enumerate(cores):
    if left % core == 0:
      processed += 1
      if processed == n:
        return i + 1