def solution(n, k, cmd):
  # 파이썬 내장 함수 'next'와의 섀도잉(충돌)을 방지하기 위해 nxt_arr 사용
  prev_arr = [i - 1 for i in range(n)]
  nxt_arr = [i + 1 for i in range(n)]
  prev_arr[0], nxt_arr[-1] = None, None

  current = k
  deleted_index = []

  for c in cmd:
    if c == 'C':
      pre, nxt = prev_arr[current], nxt_arr[current]
      deleted_index.append((pre, current, nxt))

      if pre is not None:
        nxt_arr[pre] = nxt
      if nxt is not None:
        prev_arr[nxt] = pre
        current = nxt
      else:
        current = pre

    elif c == 'Z':
      pre, curr, nxt = deleted_index.pop()

      if pre is not None:
        nxt_arr[pre] = curr
      if nxt is not None:
        prev_arr[nxt] = curr
      prev_arr[curr] = pre
      nxt_arr[curr] = nxt

    else:
      command, idx = c.split()
      count = int(idx)
      if command == 'U':
        for _ in range(count):
          current = prev_arr[current]
      else:
        for _ in range(count):
          current = nxt_arr[current]

  # 최종 결과 문자열 생성
  answer = ['O'] * n
  for _, x, _ in deleted_index:
    answer[x] = 'X'
  return ''.join(answer)