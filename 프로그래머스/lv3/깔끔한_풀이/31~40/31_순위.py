def solution(n, results):
    match_result = [['' for _ in range(n + 1)] for _ in range(n + 1)]

    for win, lose in results:
        match_result[win][lose] = 'w'
        match_result[lose][win] = 'l'

    # 플로이드-워샬 알고리즘: k를 거쳐서 i가 j를 이기는 경우 탐색
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if match_result[i][k] == 'w' and match_result[k][j] == 'w':
                    match_result[i][j] = 'w'
                    match_result[j][i] = 'l'

    # 자신을 제외한 나머지 선수들과의 승패 결과(w 또는 l)를 모두 아는 선수의 수 카운트
    return sum(1 for x in match_result[1:] if sum(1 for y in x[1:] if y in ('w', 'l')) == n - 1)