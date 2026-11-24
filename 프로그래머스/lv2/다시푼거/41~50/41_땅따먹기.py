def solution(land):
    n = len(land)
    m = len(land[0])
    
    for i in range(1, n) :
        for j in range(m) :
            land[i][j] += max(x for k, x in enumerate(land[i - 1]) if k != j)

    return max(land[-1])