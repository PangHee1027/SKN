def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x : (x[col - 1], -x[0]))
    
    answer = 0
    for i in range(row_begin, row_end + 1) :
        result = 0
        for col in data[i - 1] :
            result += col % i
        answer ^= result
    
    return answer