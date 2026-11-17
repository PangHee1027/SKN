def solution(arr1, arr2):
    answer = []
    for row1, row2 in zip(arr1, arr2) :
        row = []
        for a, b in zip(row1, row2) :
            row.append(a + b)
        answer.append(row)
        
    return answer