from collections import Counter

def solution(weights):
  answer = 0
  count = Counter(weights)

  # items()를 활용해 몸무게(key)와 인원수(cur)를 한 번에 언패킹
  for key, cur in count.items():
    # 1. 동일한 몸무게끼리 쌍을 이루는 경우 nC2 = n * (n - 1) / 2
    answer += cur * (cur - 1) // 2

    # 2. 비율 2:3 (1.5배)
    if key % 2 == 0:
      answer += count.get((key // 2) * 3, 0) * cur

    # 3. 비율 2:4 (2배)
    answer += count.get(key * 2, 0) * cur

    # 4. 비율 3:4 (4/3배)
    if key % 3 == 0:
      answer += count.get((key // 3) * 4, 0) * cur

  return answer