def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr2[0])
    answer = [] 
    for i in range(row) :
        cur_row = []
        for j in range(col) :
            cur = 0
            for k in range(len(arr2)) :
                cur += arr1[i][k] * arr2[k][j]
            cur_row.append(cur)
        answer.append(cur_row)
    return answer

print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))