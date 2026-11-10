import string

k = int(input())
rows = int(input())
target_str = input().strip()
end = list(target_str)

start = list(string.ascii_uppercase[:k])
ladder = []
target = -1

for i in range(rows):
    row_str = input().strip()
    if '?' in row_str:
        target = i
        ladder.append('?')
    else:
        ladder.append(row_str)

# 1. 위에서부터 target 줄 전까지 시뮬레이션
for i in range(target):
    for j in range(k - 1):
        if ladder[i][j] == '-':
            start[j], start[j + 1] = start[j + 1], start[j]

# 2. 아래에서부터 target 줄 다음까지 역추적 시뮬레이션
for i in range(rows - 1, target, -1):
    for j in range(k - 1):
        if ladder[i][j] == '-':
            end[j], end[j + 1] = end[j + 1], end[j]

# 3. target 줄의 가로 막대 결정
answer = []
i = 0
while i < k - 1:
    if start[i] == end[i]:
        answer.append('*')
        i += 1
    elif start[i] == end[i + 1] and start[i + 1] == end[i]:
        answer.append('-')
        # 두 줄이 교차하므로 end 상태를 갱신
        end[i], end[i + 1] = end[i + 1], end[i]
        i += 1
    else:
        # 연속된 가로 막대 규칙 위반 또는 매칭 불가
        # (주의: 사다리 특성상 인접한 위치에 연속으로 '-'가 올 수 없는 조건 등을 고려해야 합니다)
        print('x' * (k - 1))
        break
else:
    # 최종적으로 start와 end가 완전히 일치하는지 확인
    if start == end:
        print(''.join(answer))
    else:
        print('x' * (k - 1))