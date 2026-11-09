n, m = map(int, input().split())

# dp[i][j]: 합이 i이고, 사용한 숫자의 최댓값이 j 이하인 정수 분할의 수
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 1  # 합이 0일 때, 아무것도 고르지 않는 경우의 수 1

for i in range(n + 1):
  for j in range(1, m + 1):
    # 1. 숫자 j를 아예 사용하지 않는 경우 (최댓값이 j-1 이하인 경우)
    dp[i][j] = dp[i][j - 1]

    # 2. 숫자 j를 적어도 하나 사용하는 경우 (전체 합 i에서 j를 뺀 상태에서 남은 값을 채우는 경우)
    if i >= j:
      dp[i][j] = (dp[i][j] + dp[i - j][j]) % 123456789

# 합이 n이고, 최대 원소가 m 이하인 최종 편성 방법의 수 출력
print(dp[n][m])