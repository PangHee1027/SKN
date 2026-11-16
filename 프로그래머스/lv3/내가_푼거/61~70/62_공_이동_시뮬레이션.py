def solution(n, m, x, y, queries):
    min_row, max_row, min_col, max_col = x, x, y, y
    queries = reversed(queries)

    for mode, i in queries :
        match mode :
            # 0 -> 열 번호가 감소하는 방향, 역추적 -> 열번호 증가 (y +), 체크 : 왼쪽 벽
            case 0 :
                max_col = min(m - 1, max_col + i) 
                if min_col != 0 :
                    min_col = max(0, min_col + i)
                if max_col < 0 :
                    return 0 
            # 1 -> 열 번호가 증가하는 방향, 역추적 -> 열번호 감소 (y -), 체크 : 오른쪽 벽
            case 1 :
                min_col = max(0, min_col - i)
                if max_col != m - 1 :
                    max_col = min(m - 1, max_col - i) 
                if min_col >= m :
                    return 0 
            # 2 -> 행 번호가 감소하는 방향, 역추적 -> 행번호 증가 (x +), 체크 : 윗쪽 벽
            case 2 :
                max_row = min(n - 1, max_row + i)
                if min_row != 0 :
                    min_row = max(0, min_row + i)
                if max_row < 0 :
                    return 0
            # 3 -> 행 번호가 증가하는 방향, 역추적 -> 행번호 감소 (x -), 체크 : 아래쪽 벽
            case 3 :
                min_row = max(0, min_row - i)
                if max_row != n - 1 :
                    max_row = min(n - 1, max_row - i)
                if min_row >= n :
                    return 0
                
    return (max_col - min_col + 1) * (max_row - min_row + 1)

print(solution(2, 2, 0, 0, [[2,1],[0,1],[1,1],[0,1],[2,1]]))
print(solution(2, 5, 0, 1, [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]))