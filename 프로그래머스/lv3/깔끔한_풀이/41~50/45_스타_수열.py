from collections import Counter

def solution(a):
  n = len(a)
  if n < 2:
    return 0

  count = sorted(Counter(a).items(), key=lambda x: -x[1])
  answer = 0

  for key, c in count:
    if c * 2 <= answer:
      continue

    res = 0
    i = 0
    while i < n - 1:
      # 두 원소가 서로 다르고, 둘 중 하나는 반드시 현재 key여야 함
      if a[i] != a[i + 1] and (a[i] == key or a[i + 1] == key):
        res += 2
        i += 2  # 쌍을 이뤘으므로 다음 칸으로 점프
      else:
        i += 1  # 조건을 만족하지 못하면 한 칸씩 이동

    answer = max(answer, res)

  return answer