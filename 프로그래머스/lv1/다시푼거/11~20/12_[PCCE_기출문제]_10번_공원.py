def solution(mats, park):
    mats.sort(reverse = True)
    n, m = len(park), len(park[0])
    
    for mat in mats :
        for i in range(n - mat + 1) :
            for j in range(m - mat + 1) :
                if park[i][j] != '-1' :
                    continue
                if all(park[x][y] == '-1' for x in range(i, i + mat) for y in range(j, j + mat)) :
                    return mat
    return -1