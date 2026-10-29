def solution(n, results):
    match_result = [['' for _ in range(n + 1)] for _ in range(n + 1)]

    for win, lose in results :
        match_result[win][lose] = 'w'
        match_result[lose][win] = 'l'

    for _ in range(n) :
        for i in range(1, n + 1) :
            for j in range(1, n + 1) :
                if i == j :
                    continue
                cur = match_result[i][j]
                if cur == 'w' :
                    idx = []
                    for k in range(1, n + 1) :
                        if match_result[j][k] == 'w' :
                            idx.append(k)
                    for k in idx :
                        match_result[i][k] = 'w'
                        match_result[k][i] = 'l'

    return sum(1 for x in match_result if sum(1 for y in x if y in ('w', 'l')) == n - 1)

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))