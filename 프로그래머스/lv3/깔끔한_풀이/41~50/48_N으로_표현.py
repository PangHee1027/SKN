from itertools import product


def solution(N, number):
  if N == number:
    return 1

  dp = [set() for _ in range(9)]
  for i in range(1, 9):
    dp[i].add(int(str(N) * i))

  for i in range(2, 9):
    for j in range(1, i):
      k = i - j
      for num1, num2 in product(dp[j], dp[k]):
        dp[i].add(num1 + num2)
        dp[i].add(num1 * num2)
        if num1 - num2 > 0:
          dp[i].add(num1 - num2)
        if num2 != 0 and num1 // num2 > 0:
          dp[i].add(num1 // num2)

    if number in dp[i]:
      return i

  return -1