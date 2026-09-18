def solution(X, Y):
    num_x = {}
    num_y = {}
    result = []
    for i in X :
        num_x[i] = num_x.get(i, 0) + 1

    for i in Y :
        num_y[i] = num_y.get(i, 0) + 1
    
    for i in range(10) :
        result += [str(i)] * min(num_x.get(str(i), 0), num_y.get(str(i), 0))

    if len(result) == 0 :
        return "-1"
    
    result.sort(reverse = True)

    if result[0] == "0":
        return "0"
    
    result = "".join(result)

    return result

# print(solution("5525", "1255"))