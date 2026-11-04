def solution(n, build_frame) :
    def is_valid():
        for i in range(n + 1):
            for j in range(n + 1):
                if i < n and column[i][j]:
                    if not (i == 0 or (j > 0 and beam[i][j - 1]) or (j < n and beam[i][j]) or (i > 0 and column[i - 1][j])):
                        return False
                if j < n and beam[i][j]:
                    if not ((i > 0 and column[i - 1][j]) or (i > 0 and column[i - 1][j + 1]) or (j > 0 and beam[i][j - 1] and j < n - 1 and beam[i][j + 1])):
                        return False
        return True
    
    def emplace_column(i, j) :
        column[i][j] = True
        if not is_valid():
            column[i][j] = False
    
    def emplace_beam(i, j) :
        beam[i][j] = True
        if not is_valid():
            beam[i][j] = False
    
    def remove_column(i, j):
        column[i][j] = False
        if not is_valid():
            column[i][j] = True

    def remove_beam(i, j):
        beam[i][j] = False
        if not is_valid():
            beam[i][j] = True
    
    column = [[False] * (n + 1) for _ in range(n)]
    beam = [[False] * n for _ in range(n + 1)]

    for x, y, type, work in build_frame :
        if work :
            if type :
                emplace_beam(y, x)
            else :
                emplace_column(y, x)
        else :
            if type :
                remove_beam(y, x)
            else :
                remove_column(y, x)            

    answer = []

    for i, row in enumerate(column) :
        for j, col in enumerate(row) :
            if col :
                answer.append([j, i, 0])

    for i, row in enumerate(beam) :
        for j, col in enumerate(row) :
            if col :
                answer.append([j, i, 1])

    answer.sort(key = lambda x : (x[0], x[1], x[2]))
    
    return answer

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
# [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
# [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]