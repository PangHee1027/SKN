def solution(board, skill) :
    m, n = len(board), len(board[0])
    diff = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for type, r1, c1, r2, c2, degree in skill :
        diff[r1][c1] += degree * (1 if type == 2 else -1)
        diff[r1][c2+1] += degree * (-1 if type == 2 else 1)
        diff[r2+1][c1] += degree * (-1 if type == 2 else 1)
        diff[r2+1][c2+1] += degree * (1 if type == 2 else -1)

    for j in range(m) :
        for i in range(1, n) :
            diff[j][i] += diff[j][i - 1]

    for i in range(n) :
        for j in range(1, m) :
            diff[j][i] += diff[j - 1][i]

    not_broken = 0

    for i in range(m) :
        for j in range(n) :
            if diff[i][j] + board[i][j] > 0 :
                not_broken += 1

    return not_broken

print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]])) # 10
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]])) # 6