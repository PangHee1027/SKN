n = int(input())

# bricks[_][j]
## j = 0 : 인덱스, j = 1 : 넓이, j = 2 : 높이, j = 3 : 무게
bricks = []

for i in range(1, n + 1) :
    brick = list(map(int, input().split()))
    bricks.append([i] + brick)

bricks.sort(key = lambda x : x[1])

dp = [brick[2] for brick in bricks]
parent = [-1] * (n + 1)

for i in range(n):
  for j in range(i):
    if bricks[j][3] < bricks[i][3]:
      if dp[j] + bricks[i][2] > dp[i]:
        dp[i] = dp[j] + bricks[i][2]
        parent[i] = j

max_idx = dp.index(max(dp))
tower = []
curr = max_idx
while curr != -1:
  tower.append(bricks[curr][0])  # 1번 자리에 있는 원래 벽돌 번호 저장
  curr = parent[curr]

# 출력: 개수 출력 후, 위쪽 벽돌부터 차례대로(역순으로) 출력
print(len(tower))
for b in reversed(tower):
  print(b)