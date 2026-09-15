# 내가 너무 어렵게 생각했다
# a = "#" 가 존재하는 y좌표의 리스트
# b = "#" 가 존재하는 x좌표의 리스트
# a, b 각각의 최솟값을 조합한 좌표 ~ 최댓값 + 1 을 조합한 죄표면 조건을 만족함
def solution(wall):
    a, b = [], []
    for i in range(len(wall)):
        for j in range(len(wall[i])):
            if wall[i][j] == "#":
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a) + 1, max(b) + 1]