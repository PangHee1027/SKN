def solution(key, lock) :
    def rotate_key_90() :
        nonlocal key
        new_key = [[0] * n for _ in range(n)]
        for i in range(n) :
            for j in range(n) :
                new_key[j][n - 1 - i] = key[i][j]
        key = new_key
        return
    n = len(key)
    m = len(lock)
    for _ in range(4) :
        rotate_key_90()
        for k in range(-m, m, 1) :
            for l in range(-m, m, 1) :
                matrix = [[0] * m for _ in range(m)]
                for i in range(n) :
                    for j in range(n) :
                        x, y = i + k, j + l
                        if x >= m or y >= m or x < 0 or y < 0 :
                            continue
                        matrix[x][y] = key[i][j]
                for i in range(m) :
                    for j in range(m) :
                        if not lock[i][j] ^ matrix[i][j] :
                            break
                    else :
                        continue
                    break
                else :
                    return True
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))