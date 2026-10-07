def solution(m, n, board):
    answer = 0
    board_preprocessed = [[0] * m for _ in range(n)]
    for i in range(m) :
        for j in range(n) :
            board_preprocessed[j][m - i - 1] = board[i][j]
    while True :
        drop = []
        visited = set()
        for i in range(1, n) :
            for j in range(1, m) :
                if board_preprocessed[i - 1][j - 1] == board_preprocessed[i][j - 1] == board_preprocessed[i - 1][j] == board_preprocessed[i][j] != 0 :
                    for coordinate in [(i, j), (i, j - 1), (i - 1, j), (i - 1, j - 1)] :
                        if coordinate not in visited :
                            drop.append(coordinate)
                            visited.add(coordinate)
        if not drop :
            break
        answer += len(drop)
        drop.sort(key = lambda x : x[1])
        while drop :
            a, b = drop.pop()
            board_preprocessed[a].pop(b)
            board_preprocessed[a].append(0)
        
    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))