def solution(land):
    h = len(land)
    w = 4

    for i in range(1, h) :
        for j in range(w) :
            land[i][j] += max([x for y, x in enumerate(land[i -1]) if y != j])

    return max(land[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))