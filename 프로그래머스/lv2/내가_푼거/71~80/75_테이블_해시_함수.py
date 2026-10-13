def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x : x[0], reverse = True)
    data.sort(key = lambda x : x[col - 1])

    result = []

    for i in range(row_begin - 1, row_end) :
        S_i = data[i]
        for j, col in enumerate(S_i) :
            S_i[j] = col % (i + 1)
        result.append(sum(S_i))

    answer = result[0]
    for i in range(1, len(result)) :
        answer = answer ^ result[i]

    return answer

print(solution([[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3))