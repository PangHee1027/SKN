def solution(number, k):
  stack = []

  for n in number:
    # 지울 기회(k)가 있고, 스택 맨 위 숫자가 현재 숫자보다 작으면 계속 pop
    while stack and stack[-1] < n and k > 0:
      stack.pop()
      k -= 1
    stack.append(n)

  # 숫자가 내림차순이라 k가 남은 경우, 뒤에서 남은 k개 제거
  if k > 0:
    stack = stack[:-k]

  return "".join(stack)